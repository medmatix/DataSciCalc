#!/usr/bin/python3                   ## linux shell script directive
# -*- coding: utf-8 -*-              ## default character set selection

'''

DataSciCalc_oldest, Main Program Module

Created on Sep 5, 2018
@version: 0.1
@author: David A York
@ copyright: 2018
@note: revision and rewrite of SimpleCalc 1.23 as a data science desktop calculator application

@license: MIT, https://opensource.org/licenses/MIT

'''

#======================================================
# imports
#======================================================
# standard library imports
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import Canvas
from tkinter import messagebox as mBox


from os import path, makedirs
import time
from datetime import datetime
import math


# module imports
from ActionFunctions import ActionFunctions as af

# ~~~ End import section ~~~ =================


# ===================================
# GlobalVariables and Constants
# ===================================

# module level  GLOBALS
inxRegStr = ''
inLRegStrg = ('')
x = 0.0
y = 0.0
L = (0.0)
resVar = 0.0
xFlag = False
Lflag = False
# logHistoryName = "historyLog"

## ~~~ END of Glogal Declarations ~~ =================


#=====================================================
# Class definitions
#=====================================================

class calcGUI():
    ''' 
    GUI building gui elements, element activation functions and variables for calcGUI Class
    
    '''
    
    
    # Class Constructor ------------------------------
    def __init__(self):


        self.inxRegStr = ''
        self.inLRegStr = ('')
        self.x = 0.0
        self.y = 0.0
        self.L = (0.0)
        self.resVar = 0.0
        self.xFlag = False
        self.Lflag = False   
        
        # Create instance
        self.win = tk.Tk()
           
        # Add a title
        self.win.title("Data Science Calculator")
        
        # Add a icon
        self.win.iconbitmap('./images/Number_cruncherCr2.ico')
        
        # Initialize widgets
        self.createWidgets()
        self.inxStr.focus()
    # ~~~ End class contruction / initializer ~~-----
    
    
    # == GUI widget Functions and Definitions =================================
    # -- Exit GUI cleanly -------------
    def _quit(self):
        self.win.quit()
        self.win.destroy()
        print('run is done, exited normally!')
        exit()
    
    # -- make an messages and messageBoxes for GUI help and errors
    def info(self):
        mBox.showinfo('About DataSciCalc_oldest', 'A Data Science Calculator\n (c) David A York, 2018\n http:crunches-data.appspot.com \nVersion: 1.23, development version\nlicense: MIT/X-Windows')

    # catch trying to cast a blank to a number
    def castError(self):
        mBox.showwarning(title= "Ooops!!!", message="The Input field can't be blank or non-mumeric \na number should be entered first, then ENTER.\n\nREVERSE POLISH Notation (RPN) means: enter all numbers, THEN choose an operation.The result is always brought forward as follow-up input in case needed\nOperations can be chained by just entering next input.")
    
    def improperInputError(self):
        mBox.showerror(title= "Ooops!!!", message="Improper Operand, did you try to take a log of a negative or to divide by zero, etc.")
    
    def arithmeticError(self):
        mBox.showerror(title= "Ooops!!!", message="you need to enter value before selecting an operation")
        
    def underConstruction(self):
        mBox.showinfo(title= "Men at Work!!", message="This function has not been implemented yet, \nsorrrrrrry - see next version :)")
        
    # -- make history display dialog and print 
    def historyToDialog(self):
        mBox._show(title="History", message=self.history.get(1.0, tk.END), _icon="", _type="")
    
    def notesToDialog(self):
        mBox._show(title="Notes", message=self.scr_notes.get(1.0, tk.END), _icon='', _type="")
        
        
    # == GUI widget constructiom ==============================================
    def createWidgets(self):        
        
        # Tab Controls introduced here --------------------------------------
        tabControl = ttk.Notebook(self.win)     # Create Tab Control

        tab1 = ttk.Frame(tabControl)            # Create a tab
        tabControl.add(tab1, text='Calculator')      # Add the tab

        tab2 = ttk.Frame(tabControl)            # Add a second tab
        tabControl.add(tab2, text='Notes')      # Make second tab visible
        
        tab3 = ttk.Frame(tabControl)            # Add a third tab
        tabControl.add(tab3, text='Documentation')      # Make third tab visible
        
        tab4 = ttk.Frame(tabControl)            # Add a fourth tab
        tabControl.add(tab4, text='Statistics')      # Make fourth tab visible
         
        tab5 = ttk.Frame(tabControl)            # Add a fifth tab
        tabControl.add(tab5, text='Graphics')      # Make fourth tab visible

        tabControl.pack(expand=1, fill="both")  # Pack to make visible
        # ~ end ~ Tab Controls introduced here -----------------------------------------


        #  We are creating a container frame to tab1 widgets ============================
        self.display = ttk.LabelFrame(tab1, text=' Inputs ')
        self.display.grid(column=0, row=0, padx=8, pady=4)
        
        self.inputAction = ttk.LabelFrame(tab1, text=' Input Action ')
        self.inputAction.grid(column=0, row=5, padx=8, pady=4)
        
        # We are creating a frame to hold the a data block of text
        self.inKeys = ttk.LabelFrame(tab1, text=' Number Keys ')
        self.inKeys.grid(column=0, row=10, padx=8, pady=4)
        
        self.functKeys = ttk.LabelFrame(tab1, text=' Function Keys ')
        self.functKeys.grid(column=0, row=18, padx=8, pady=8)
        
 
        # Adding a Entry widget for x input
        ttk.Label(self.display, text="  x ").grid(column=0, row=0, padx=4, pady=4,sticky='W')
        self.inxStr = ttk.Entry(self.display, width=68, text='x')
        self.inxStr.grid(column=1, row=0, padx=4, pady=4,sticky='W')
          
        # Scrolling input field for L or y entry ( L is list of sequence entered, y is single number entered:
        # Using a scrolled Text control for List entry
        scrolW1  = 30; scrolH1  =  2
        ttk.Label(self.display, text="List").grid(column=0, row=2, padx=4, pady=4,sticky='W')
        self.inLStr = scrolledtext.ScrolledText(self.display, width=scrolW1, height=scrolH1, wrap=tk.WORD)
        self.inLStr.grid(column=1, row=2, padx=4, pady=4, sticky='WE', columnspan=3)
        
        # House keeping function buttons
        
        self.clrx = ttk.Button(self.inputAction, text=" CLR x ", command=lambda: af.do_clrx(self))
        self.clrx.grid(column=0, row=0, padx=4, pady=4)

        self.clrL = ttk.Button(self.inputAction, text=" CLR L ", command=lambda: af.do_clrL(self))
        self.clrL.grid(column=1, row=0, padx=4, pady=4)
        
        self.toList = ttk.Button(self.inputAction, text="  ENTER L  ", command=lambda: af.do_enterL(self))
        self.toList.grid(column=2, row=0, padx=4, pady=4)
        
        self.action_toxVar = ttk.Button(self.inputAction, text="ENTER x", command=lambda: af.do_enterx(self))
        self.action_toxVar.grid(column=3, row=0, padx=4, pady=6)

        # Populate inKeys frame with the digit input keys (buttons)
        # Adding digit entry buttons 1 to 3
        
        self.action1 = ttk.Button(self.inKeys, text=" 1 ", command=lambda: af.append_digit1(self))
        self.action1.grid(column=0, row=0, padx=4, pady=2)

        self.action2 = ttk.Button(self.inKeys, text=" 2 ", command=lambda: af.append_digit2(self))
        self.action2.grid(column=1, row=0, padx=4, pady=2)
        
        self.action3 = ttk.Button(self.inKeys, text=" 3 ", command=lambda: af.append_digit3(self))
        self.action3.grid(column=2, row=0, padx=4, pady=2)
        # Adding digit entry buttons 1 to 3
        self.action4 = ttk.Button(self.inKeys, text=" 4 ", command=lambda: af.append_digit4(self))
        self.action4.grid(column=0, row=2, padx=4, pady=2)

        self.action5 = ttk.Button(self.inKeys, text=" 5 ", command=lambda: af.append_digit5(self))
        self.action5.grid(column=1, row=2, padx=4, pady=2)
        
        self.action6 = ttk.Button(self.inKeys, text=" 6 ", command=lambda: af.append_digit6(self))
        self.action6.grid(column=2, row=2, padx=4, pady=2)
        # Adding digit entry buttons 1 to 3
        self.action7 = ttk.Button(self.inKeys, text=" 7 ", command=lambda: af.append_digit7(self))
        self.action7.grid(column=0, row=4, padx=4, pady=2)

        self.action8 = ttk.Button(self.inKeys, text=" 8 ", command=lambda: af.append_digit8(self))
        self.action8.grid(column=1, row=4, padx=4, pady=2)
        
        self.action9 = ttk.Button(self.inKeys, text=" 9 ", command=lambda: af.append_digit9(self))
        self.action9.grid(column=2, row=4, padx=4, pady=2)
        
        self.action_pi = ttk.Button(self.inKeys, text=" pi ", command=lambda: af.get_pi(self))
        self.action_pi.grid(column=0, row=6, padx=4, pady=2)
        
        self.action0 = ttk.Button(self.inKeys, text=" 0 ", command=lambda: af.append_digit0(self))
        self.action0.grid(column=1, row=6, padx=4, pady=2)  
        
        self.action_e = ttk.Button(self.inKeys, text=" e ", command=lambda: af.get_e(self))
        self.action_e.grid(column=2, row=6, padx=4, pady=2)
                
        self.action_pi = ttk.Button(self.inKeys, text=" - ", command=lambda: af.get_pi(self))
        self.action_pi.grid(column=0, row=7, padx=4, pady=2)
        
        self.actiondec = ttk.Button(self.inKeys, text=" . ", command=lambda: af.append_dec(self))
        self.actiondec.grid(column=1, row=7, padx=4, pady=2)
        
        self.action_phi = ttk.Button(self.inKeys, text=" , ", command=lambda: af.get_phi(self))
        self.action_phi.grid(column=2, row=7, padx=4, pady=2)
        

     
        #Populate function keys frame
        self.action_add = ttk.Button(self.functKeys, text=" L + x ", command=lambda: af.do_add(self))
        self.action_add.grid(column=0, row=0, padx=4, pady=6)

        self.action_subt = ttk.Button(self.functKeys, text=" L - x ", command=lambda: af.do_subt(self))
        self.action_subt.grid(column=1, row=0, padx=4, pady=6)
        
        self.action_mult = ttk.Button(self.functKeys, text=" L * x ", command=lambda: af.do_mult(self))
        self.action_mult.grid(column=2, row=0, padx=4, pady=6)
        
        self.action_div = ttk.Button(self.functKeys, text=" L / x ", command=lambda: af.do_div(self))
        self.action_div.grid(column=3, row=0, padx=4, pady=6)
        
        self.action_sumL = ttk.Button(self.functKeys, text=" sum L ", command=lambda: af.do_xpowy(self))
        self.action_sumL.grid(column=0, row=1, padx=4, pady=6)

        self.action_prodL = ttk.Button(self.functKeys, text=" prod L ", command=lambda: af.do_sqrt(self))
        self.action_prodL.grid(column=1, row=1, padx=4, pady=6)
        
        self.action_inverseL = ttk.Button(self.functKeys, text=" 1/L ", command=lambda: af.do_invert(self))
        self.action_inverseL.grid(column=2, row=1, padx=4, pady=6)
        
        self.action_Lpowerx = ttk.Button(self.functKeys, text=" L^2 ", command=lambda: af.do_power2(self))
        self.action_Lpowerx.grid(column=3, row=1, padx=4, pady=6)
        
        self.action_sin = ttk.Button(self.functKeys, text="sin", command=lambda: af.do_sin(self))
        self.action_sin.grid(column=0, row=2, padx=4, pady=6)
        
        self.action_cos = ttk.Button(self.functKeys, text="cos", command=lambda: af.do_cos(self))
        self.action_cos.grid(column=1, row=2, padx=4, pady=6)
        
        self.action_tan = ttk.Button(self.functKeys, text="tan", command=lambda: af.do_tan(self))
        self.action_tan.grid(column=2, row=2, padx=4, pady=6)
        
        self.action_acos = ttk.Button(self.functKeys, text="acos", command=lambda: af.do_acos(self))
        self.action_acos.grid(column=3, row=2, padx=4, pady=6)
        
        self.action_asin = ttk.Button(self.functKeys, text="asin", command=lambda: af.do_asin(self))
        self.action_asin.grid(column=0, row=3, padx=4, pady=6)
        
        self.action_atan = ttk.Button(self.functKeys, text="atan", command=lambda: af.do_atan(self))
        self.action_atan.grid(column=1, row=3, padx=4, pady=6)
        
        self.action_log10L = ttk.Button(self.functKeys, text=" log10 L", command=lambda: af.do_log10(self))
        self.action_log10L.grid(column=2, row=3, padx=4, pady=6)
        
        self.action_10powL = ttk.Button(self.functKeys, text=" 10^L", command=lambda: af.do_log10(self))
        self.action_10powL.grid(column=3, row=3, padx=4, pady=6)
        
        self.action_lnL = ttk.Button(self.functKeys, text=" ln L ", command=lambda: af.do_ln(self))
        self.action_lnL.grid(column=0, row=4, padx=4, pady=6)
        
        self.action_expL = ttk.Button(self.functKeys, text="exp(L)", command=lambda: af.do_exp(self))
        self.action_expL.grid(column=1, row=4, padx=4, pady=6)
        
        self.action_xroot = ttk.Button(self.functKeys, text="L^1/x", command=lambda: af.do_exp(self))
        self.action_xroot.grid(column=2, row=4, padx=4, pady=6)
        
        self.action_Lpowx = ttk.Button(self.functKeys, text="L^x", command=lambda: af.do_exp(self))
        self.action_Lpowx.grid(column=3, row=4, padx=4, pady=6)
        
        self.action_xchL = ttk.Button(self.functKeys, text="x <> L", command=lambda: af.do_exp(self))
        self.action_xchL.grid(column=0, row=5, padx=4, pady=6)
        
        self.action_deg2rad = ttk.Button(self.functKeys, text="deg>rad", command=lambda: af.do_deg2rad(self))
        self.action_deg2rad.grid(column=1, row=5, padx=4, pady=6)
        
        self.action_sgn = ttk.Button(self.functKeys, text=" +/- ", command=lambda: af.do_sgn(self))
        self.action_sgn.grid(column=2, row=5, padx=4, pady=6)
        
        self.action_blank = ttk.Button(self.functKeys, text="  ", command=lambda: af.do_blank(self))
        self.action_blank.grid(column=3, row=5, padx=4, pady=6)
        
        #=======================================================================
        # self.action_unasgn = ttk.Button(self.functKeys, text="unasgn", command=lambda: af.do_blank(self))
        # self.action_unasgn.grid(column=4, row=2, padx=4, pady=6)
        #=======================================================================
        

        
        # We are creating a container frame to hold tab2 widgets ============================
        self.notes = ttk.LabelFrame(tab2, text=' Notes ')
        self.notes.grid(column=0, row=0, padx=8, pady=4, sticky='W')
        
        self.notesctl = ttk.LabelFrame(self.notes)
        self.notesctl.grid(column=0, row=0, padx=8, pady=4, sticky='W')
        
        scrolW1  = 50; scrolH1  =  20
        self.scr_notes = scrolledtext.ScrolledText(self.notes, width=scrolW1, height=scrolH1, wrap=tk.WORD)
        self.scr_notes.grid(column=0, row=6, padx=4, pady=4, sticky='WE', columnspan=3)
        
        self.action_clrnotes = ttk.Button(self.notesctl, text="CLEAR", command=lambda: af.do_clr_notes(self, self.scr_notes))
        self.action_clrnotes.grid(column=0, row=0, padx=4, pady=6)
        
        self.action_prtnotes = ttk.Button(self.notesctl, text="PRINT", command=lambda: af.do_prt_notes(self, self.scr_notes))
        self.action_prtnotes.grid(column=1, row=0, padx=4, pady=6)
        
        self.action_lognotes = ttk.Button(self.notesctl, text="LOG IT", command=lambda: af.do_log_notes(self))
        self.action_lognotes.grid(column=2, row=0, padx=4, pady=6)
        self.action_savenotes = ttk.Button(self.notesctl, text="SAVE", command=lambda: af.do_save_notes(self))
        self.action_savenotes.grid(column=3, row=0, padx=4, pady=6)
        self.action_menunotes = ttk.Button(self.notesctl, text="MENU", command=lambda: af.do_note(self))
        self.action_menunotes.grid(column=4, row=0, padx=4, pady=6)
        
        
        
        
        # We are creating a container frame to hold tab3 widgets ============================
        self.documentation = ttk.LabelFrame(tab3, text=' The Manual ')
        self.documentation.grid(column=0, row=3, padx=8, pady=4, sticky='W')
        
        # the index of the manual
        ttk.Label(self.documentation, text="Manual Sections:").grid(column=0, row=0)
        self.choice = tk.StringVar()
        self.indexChosen = ttk.Combobox(self.documentation, width=65, textvariable=self.choice)
        self.indexChosen['values'] = ('All', 'Overview', 'Introduction', 'Operations', 'Functions', 'References', 'Further Explorations')
        self.indexChosen.current(0)
        self.indexChosen.grid(column=0, row=1)
        
        # The Manual text                
        # Scrolling Documentation field:
        # Creating a Label
        ttk.Label(self.documentation, text="Documentation:").grid(column=0, row=5, sticky='W')
        
        # Using a scrolled Text control for review of documentation
        scrolW1  = 50; scrolH1  =  30
        self.manual = scrolledtext.ScrolledText(self.documentation, width=scrolW1, height=scrolH1, wrap=tk.WORD)
        self.manual.grid(column=0, row=6, padx=4, pady=4, sticky='WE', columnspan=3)
        section = "./documentation/all_docs.txt"
        docFile=open(section, 'r')
        self.manual.insert(tk.INSERT, '\n' + docFile.read())
        
        # Creating a container frame to hold tab4 widgets
        self.statistics = ttk.LabelFrame(tab4, text=' A Statistical Applications Interface ')
        self.statistics.grid(column=0, row=3, padx=8, pady=4, sticky='W')
        ttk.Label(self.statistics, text="Statistics:  this application functionality has not yet been implemented ........        ").grid(column=0, row=5, sticky='W')
          
        
        # Creating a container frame to hold tab5 graphing widgets 
        self.graphical = ttk.LabelFrame(tab5, text=' Graphical Output ')
        self.graphical.grid(column=0, row=0, padx=8, pady=4)
         
        # Adding a graphic window (canvas widget)
        gw = Canvas(self.graphical, width=415, height=550)
        gw.create_text(60,10, text="Not yet implemented")
        gw.grid(column=0, row=1, padx=8, pady=4, sticky='W')
               
        
        # Creating a Menu Bar ---------------------------------------------------------------------
        menuBar = Menu(tab1)
        self.win.config(menu=menuBar)

        # Add menu items
        fileMenu = Menu(menuBar, tearoff=0)
        fileMenu.add_command(label="New")
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self._quit)
        menuBar.add_cascade(label="File", menu=fileMenu)
        
        # Add an Edit Menu
        editMenu = Menu(menuBar, tearoff=0)
        editMenu.add_command(label="Cut")
        editMenu.add_command(label="Copy")
        editMenu.add_command(label="Paste")
        editMenu.add_separator()
        editMenu.add_command(label="Options")
        menuBar.add_cascade(label="Edit", menu=editMenu)

        # Add another Menu to the Menu Bar and an item
        helpMenu = Menu(menuBar, tearoff=0)
        helpMenu.add_command(label="Context Help")
        helpMenu.add_command(label="Documentation")
        helpMenu.add_command(label="About", command=self.info)
        menuBar.add_cascade(label="Help", menu=helpMenu)

        # ~ end of menu bar ~ ------------------------------------------------- 
        # Change the main windows icon
        #self.win.iconbitmap(r'C:\Python34\DLLs\pyc.ico')

        # Place cursor into name Entry
        #nameEntered.focus()
        
        # Set Focus to Tab2
        tabControl.select(0)


        # Add a Tooltip to the Spinbox
# ~~ End of TKGUI CLass =======================================================        
        
        

#======================
# Start GUI
#======================
# tkgui = TKGUI()

#running methods in threads
#runT=Thread(target=oop.methodInAThread)

# tkgui.win.mainloop()

# ===============================================
# Unit Testing Code
# ===============================================
if __name__ == '__main__':
    print("tkGUI is running as main; \n    ie. a module self test")
    tkgui = calcGUI()
    tkgui.win.mainloop()
#~~~ END test code ==============================