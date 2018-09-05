# -*- coding: utf-8 -*-
'''

DataSciCalc, Main Program Module

Created on Sep 5, 2018
@version: 0.0
@author: David A York
@ copyright: 2018
@note: revision and rewrite of SimpleCalc 1.23 as a data science desktop calculator application

@license: LGPL, https://www.gnu.org/licenses/lgpl.html 

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
from math import sqrt
# module imports


# ~~~ End import section ~~~ =================


# ===================================
# GlobalVariables and Constants
# ===================================

# module level  GLOBALS
currentRegisterStr = ''
currentVariable = 0.0
operandTwo = 0.0
operandThree = 0.0
resultVariable = 0.0
entFlag = False
logHistoryName = "historyLog"

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
        self.currentRegisterStr = ''
        self.currentVariable = 0.0
        self.operandTwo = 0.0
        self.operandThree = 0.0
        self.resultVariable = 0.0
        self.entFlag = False
        self.logHistoryName = "historyLog"
   
        
        # Create instance
        self.win = tk.Tk()
           
        # Add a title
        self.win.title("Simple Calculator")
        
        # Add a icon
        self.win.iconbitmap('./images/Number_cruncherCr2.ico')
        
        # Initialize widgets
        self.createWidgets()
        self.inReg.focus()
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
        mBox.showinfo('About SimpleCalc', 'A Simple Python RPN Calculator\n (c) David A York, 2018\n http:crunches-data.appspot.com \nVersion: 1.23, development version\nlicense: MIT/X-Windows')

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
        
        #=======================================================================
        # tab4 = ttk.Frame(tabControl)            # Add a fourth tab
        # tabControl.add(tab4, text='Statistics')      # Make fourth tab visible
        # 
        # tab5 = ttk.Frame(tabControl)            # Add a fifth tab
        # tabControl.add(tab5, text='Graphics')      # Make fourth tab visible
        #=======================================================================

        tabControl.pack(expand=1, fill="both")  # Pack to make visible
        # ~ end ~ Tab Controls introduced here -----------------------------------------


        #  We are creating a container frame to tab1 widgets ============================
        self.display = ttk.LabelFrame(tab1, text=' Display Registers ')
        self.display.grid(column=0, row=0, padx=8, pady=4)
        
        self.clears = ttk.LabelFrame(tab1)
        self.clears.grid(column=0, row=5, padx=8, pady=4)
        
        # We are creating a frame to hold the a data block of text
        self.inKeys = ttk.LabelFrame(tab1, text=' Number Keys ')
        self.inKeys.grid(column=0, row=10, padx=8, pady=4)
        
        self.operKeys = ttk.LabelFrame(tab1, text=' Operator Keys ')
        self.operKeys.grid(column=0, row=16, padx=8, pady=4)
        
        self.functKeys = ttk.LabelFrame(tab1, text=' Function Keys ')
        self.functKeys.grid(column=0, row=18, padx=8, pady=8)
        # Input field = current register
        # Creating a Label
        ttk.Label(self.display, text="Input Field:").grid(column=0, row=0, sticky='W')
 
        # Adding a Textbox Entry widget
        self.inReg = ttk.Entry(self.display, width=68, text='Enter a number')
        self.inReg.grid(column=0, row=1, sticky='W')
          
        # Scrolling history field:
        # Creating a Label
        ttk.Label(self.display, text="Calculation History:").grid(column=0, row=3, sticky='W')
        
        # Using a scrolled Text control for review of action history
        scrolW1  = 50; scrolH1  =  4
        self.history = scrolledtext.ScrolledText(self.display, width=scrolW1, height=scrolH1, wrap=tk.WORD)
        self.history.grid(column=0, row=4, padx=4, pady=4, sticky='WE', columnspan=3)
        
        # House keeping function buttons
        
        self.clrCurReg = ttk.Button(self.clears, text=" CE ", command=lambda: ActionFunctions.do_clrCurRegr(self))
        self.clrCurReg.grid(column=0, row=0, padx=4, pady=4)

        self.clrAllReg = ttk.Button(self.clears, text=" CLR ", command=lambda: ActionFunctions.do_clrAllRegr(self))
        self.clrAllReg.grid(column=1, row=0, padx=4, pady=4)
        
        self.prtHx = ttk.Button(self.clears, text=" PrtHx ", command=lambda: ActionFunctions.do_prtHistory(self))
        self.prtHx.grid(column=2, row=0, padx=4, pady=4)
        
        self.clrHx = ttk.Button(self.clears, text=" CLHx ", command=lambda: ActionFunctions.do_clrHistory(self))
        self.clrHx.grid(column=3, row=0, padx=4, pady=4)

        # Populate inKeys frame with the digit input keys (buttons)
        # Adding digit entry buttons 1 to 3
        
        self.action1 = ttk.Button(self.inKeys, text=" 1 ", command=lambda: ActionFunctions.append_digit1(self))
        self.action1.grid(column=0, row=0, padx=4, pady=2)

        self.action2 = ttk.Button(self.inKeys, text=" 2 ", command=lambda: ActionFunctions.append_digit2(self))
        self.action2.grid(column=1, row=0, padx=4, pady=2)
        
        self.action3 = ttk.Button(self.inKeys, text=" 3 ", command=lambda: ActionFunctions.append_digit3(self))
        self.action3.grid(column=2, row=0, padx=4, pady=2)
        # Adding digit entry buttons 1 to 3
        self.action4 = ttk.Button(self.inKeys, text=" 4 ", command=lambda: ActionFunctions.append_digit4(self))
        self.action4.grid(column=0, row=2, padx=4, pady=2)

        self.action5 = ttk.Button(self.inKeys, text=" 5 ", command=lambda: ActionFunctions.append_digit5(self))
        self.action5.grid(column=1, row=2, padx=4, pady=2)
        
        self.action6 = ttk.Button(self.inKeys, text=" 6 ", command=lambda: ActionFunctions.append_digit6(self))
        self.action6.grid(column=2, row=2, padx=4, pady=2)
        # Adding digit entry buttons 1 to 3
        self.action7 = ttk.Button(self.inKeys, text=" 7 ", command=lambda: ActionFunctions.append_digit7(self))
        self.action7.grid(column=0, row=4, padx=4, pady=2)

        self.action8 = ttk.Button(self.inKeys, text=" 8 ", command=lambda: ActionFunctions.append_digit8(self))
        self.action8.grid(column=1, row=4, padx=4, pady=2)
        
        self.action9 = ttk.Button(self.inKeys, text=" 9 ", command=lambda: ActionFunctions.append_digit9(self))
        self.action9.grid(column=2, row=4, padx=4, pady=2)
        
        self.actionmin = ttk.Button(self.inKeys, text=" - ", command=lambda: ActionFunctions.append_minsgn(self))
        self.actionmin.grid(column=0, row=6, padx=4, pady=2)     
        
        self.action0 = ttk.Button(self.inKeys, text=" 0 ", command=lambda: ActionFunctions.append_digit0(self))
        self.action0.grid(column=1, row=6, padx=4, pady=2)  
        
        self.actiondec = ttk.Button(self.inKeys, text=" . ", command=lambda: ActionFunctions.append_dec(self))
        self.actiondec.grid(column=2, row=6, padx=4, pady=2)
        
        self.action_pi = ttk.Button(self.inKeys, text=" pi ", command=lambda: ActionFunctions.get_pi(self))
        self.action_pi.grid(column=0, row=7, padx=4, pady=2)
        
        self.action_e = ttk.Button(self.inKeys, text=" e ", command=lambda: ActionFunctions.get_e(self))
        self.action_e.grid(column=1, row=7, padx=4, pady=2)
        
        self.action_phi = ttk.Button(self.inKeys, text="phi", command=lambda: ActionFunctions.get_phi(self))
        self.action_phi.grid(column=2, row=7, padx=4, pady=2)
        
        
        #Populate operator keys frame
        # Adding
        self.action_add = ttk.Button(self.operKeys, text=" + ", command=lambda: ActionFunctions.do_add(self))
        self.action_add.grid(column=0, row=0, padx=4, pady=6)

        self.action_subt = ttk.Button(self.operKeys, text=" - ", command=lambda: ActionFunctions.do_subt(self))
        self.action_subt.grid(column=1, row=0, padx=4, pady=6)
        
        self.action_mult = ttk.Button(self.operKeys, text=" * ", command=lambda: ActionFunctions.do_mult(self))
        self.action_mult.grid(column=2, row=0, padx=4, pady=6)
        
        self.action_div = ttk.Button(self.operKeys, text=" / ", command=lambda: ActionFunctions.do_div(self))
        self.action_div.grid(column=4, row=0, padx=4, pady=6)
        
        self.action_equal = ttk.Button(self.operKeys, text="ENTER", command=lambda: ActionFunctions.do_enterReg(self))
        self.action_equal.grid(column=5, row=0, padx=4, pady=6)
        
        #=======================================================================
        # # bind <return/enter key to enter button
        # def areturntab1(event):
        #     ActionFunctions.do_enterReg(self)
        #     self.inReg.bind("<Return>", areturntab1)
        # 
        # def areturntab2(event):
        #     ActionFunctions.do_enterReg(self)
        #     self.tab2.bind("<Return>", areturntab2) 
        #=======================================================================
        
        #Populate function keys frame
        # Adding
        self.action_xpowy = ttk.Button(self.functKeys, text=" x**y ", command=lambda: ActionFunctions.do_xpowy(self))
        self.action_xpowy.grid(column=0, row=0, padx=4, pady=6)

        self.action_sqrt = ttk.Button(self.functKeys, text=" sqrt ", command=lambda: ActionFunctions.do_sqrt(self))
        self.action_sqrt.grid(column=1, row=0, padx=4, pady=6)
        
        self.action_inverse = ttk.Button(self.functKeys, text=" 1/x ", command=lambda: ActionFunctions.do_invert(self))
        self.action_inverse.grid(column=2, row=0, padx=4, pady=6)
        
        self.action_power2 = ttk.Button(self.functKeys, text=" **2 ", command=lambda: ActionFunctions.do_power2(self))
        self.action_power2.grid(column=3, row=0, padx=4, pady=6)
        
        self.action_sgn = ttk.Button(self.functKeys, text="+/-", command=lambda: ActionFunctions.do_sgn(self))
        self.action_sgn.grid(column=4, row=0, padx=4, pady=6)
        
        self.action_cos = ttk.Button(self.functKeys, text="cos", command=lambda: ActionFunctions.do_cos(self))
        self.action_cos.grid(column=0, row=1, padx=4, pady=6)
        
        self.action_sin = ttk.Button(self.functKeys, text="sin", command=lambda: ActionFunctions.do_sin(self))
        self.action_sin.grid(column=1, row=1, padx=4, pady=6)
        
        self.action_tan = ttk.Button(self.functKeys, text="tan", command=lambda: ActionFunctions.do_tan(self))
        self.action_tan.grid(column=2, row=1, padx=4, pady=6)
        
        self.action_acos = ttk.Button(self.functKeys, text="acos", command=lambda: ActionFunctions.do_acos(self))
        self.action_acos.grid(column=3, row=1, padx=4, pady=6)
        
        self.action_asin = ttk.Button(self.functKeys, text="asin", command=lambda: ActionFunctions.do_asin(self))
        self.action_asin.grid(column=4, row=1, padx=4, pady=6)
        
        self.action_atan = ttk.Button(self.functKeys, text="atan", command=lambda: ActionFunctions.do_atan(self))
        self.action_atan.grid(column=0, row=2, padx=4, pady=6)
        
        self.action_log10 = ttk.Button(self.functKeys, text=" log10", command=lambda: ActionFunctions.do_log10(self))
        self.action_log10.grid(column=1, row=2, padx=4, pady=6)
        
        self.action_ln = ttk.Button(self.functKeys, text=" ln ", command=lambda: ActionFunctions.do_ln(self))
        self.action_ln.grid(column=2, row=2, padx=4, pady=6)
        
        self.action_exp = ttk.Button(self.functKeys, text="exp(x)", command=lambda: ActionFunctions.do_exp(self))
        self.action_exp.grid(column=3, row=2, padx=4, pady=6)
        
        self.action_deg2rad = ttk.Button(self.functKeys, text="deg>rad", command=lambda: ActionFunctions.do_deg2rad(self))
        self.action_deg2rad.grid(column=4, row=2, padx=4, pady=6)
        
        #=======================================================================
        # self.action_unasgn = ttk.Button(self.functKeys, text="unasgn", command=lambda: ActionFunctions.do_blank(self))
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
        
        self.action_clrnotes = ttk.Button(self.notesctl, text="CLEAR", command=lambda: ActionFunctions.do_clr_notes(self, self.scr_notes))
        self.action_clrnotes.grid(column=0, row=0, padx=4, pady=6)
        
        self.action_prtnotes = ttk.Button(self.notesctl, text="PRINT", command=lambda: ActionFunctions.do_prt_notes(self, self.scr_notes))
        self.action_prtnotes.grid(column=1, row=0, padx=4, pady=6)
        
        self.action_lognotes = ttk.Button(self.notesctl, text="LOG IT", command=lambda: ActionFunctions.do_log_notes(self))
        self.action_lognotes.grid(column=2, row=0, padx=4, pady=6)
        self.action_savenotes = ttk.Button(self.notesctl, text="SAVE", command=lambda: ActionFunctions.do_save_notes(self))
        self.action_savenotes.grid(column=3, row=0, padx=4, pady=6)
        self.action_menunotes = ttk.Button(self.notesctl, text="MENU", command=lambda: ActionFunctions.do_note(self))
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
        #=======================================================================
        # self.statistics = ttk.LabelFrame(tab4, text=' A Statistical Applications Interface ')
        # self.statistics.grid(column=0, row=3, padx=8, pady=4, sticky='W')
        # ttk.Label(self.statistics, text="Statistics:  this application functionality has not yet been implemented ........        ").grid(column=0, row=5, sticky='W')
        #  
        #=======================================================================
        
        # Creating a container frame to hold tab5 graphing widgets 
        #=======================================================================
        #       self.graphical = ttk.LabelFrame(tab5, text=' Graphical Output ')
        #       self.graphical.grid(column=0, row=0, padx=8, pady=4)
        # 
        #       # Adding a graphic window (canvas widget)
        #       gw = Canvas(self.graphical, width=415, height=550)
        #       gw.create_text(60,10, text="Not yet implemented")
        #       gw.grid(column=0, row=1, padx=8, pady=4, sticky='W')
        #       
        #=======================================================================
        
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
        
        
class ActionFunctions():
    '''
    GUI element activation Function calls, actions called in response to button presses
    General Mathematical and Statistical helper Functions for callbacks etc.
    
    '''

    '''
    Constructor for ActionFunction selt tests

    '''
    def __init__(self):
        print("initialized ActionFunctions")

    # module variables and constants 

    ''' Register and variable cleanup functions '''
    def do_clrCurRegr(self):
        # clear the entry in the current input register
        self.currentRegisterStr = ''
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, self.currentRegisterStr)
        print('cleared current register')

    def do_clrAllRegr(self):
        # clear all the registers and variables for a  new calculation stream
        self.currentRegisterStr = ''
        self.inReg.delete(0, tk.END)
        self.currentVariable = 0.0
        self.operandTwo = 0.0
        self.operandThree = 0.0
        self.resultVariable = 0.0
        # log action to history 
        self.history.insert(tk.END, 'CLEAR ALL  ' + str(self.resultVariable) + '\n')
        self.history.see(tk.END)
        self.inReg.insert(tk.INSERT, self.currentRegisterStr)
        print('cleared all registers and variables')
        print('current Register: ' + self.currentRegisterStr)
        print('current Variable: ' + str(self.currentVariable))
        print('Operand 2 Variable: ' + str(self.operandTwo))
    
    def do_clrHistory(self):
        # clear the calculation history
        self.history.delete(1.0,tk.END)
        #self.history.insert(tk.END, 'CLEAR HISTORY\n')
        self.history.see(tk.END)
        print('cleared the calculation history')
        
    def do_prtHistory(self):
        print("\n Calculation history:\n")
        print(self.history.get(1.0, tk.END) + '\n')  # to Console
        self.history.insert(tk.END, 'PRINT HISTORY\n')
        self.history.see(tk.END)
        self.historyToDialog()  # and show in a dialog
        
    # appending digits to input    
    
    def append_digit0(self):        
        self.currentRegisterStr = self.currentRegisterStr +'0'        
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, self.currentRegisterStr)    
        self.entFlag = False
        print(self.currentRegisterStr)  
        print(0)            # check on value
        
    def append_digit1(self):        
        self.currentRegisterStr = self.currentRegisterStr + '1' 
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, self.currentRegisterStr)  
        self.entFlag = False  
        print(self.currentRegisterStr)              # check on value
        print(1)    
        
    def append_digit2(self):
        self.currentRegisterStr = self.currentRegisterStr + '2'        
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, self.currentRegisterStr)    
        self.entFlag = False
        print(self.currentRegisterStr) 
        print(2)
        
    def append_digit3(self):
        self.currentRegisterStr = self.currentRegisterStr + '3'        
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, self.currentRegisterStr)
        self.entFlag = False
        print(self.currentRegisterStr) 
        print(3)
        
    def append_digit4(self):
        self.currentRegisterStr = self.currentRegisterStr + '4'        
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, self.currentRegisterStr)
        self.entFlag = False
        print(self.currentRegisterStr) 
        print(4)    
        
    def append_digit5(self):
        self.currentRegisterStr = self.currentRegisterStr + '5'        
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, self.currentRegisterStr)
        self.entFlag = False
        print(self.currentRegisterStr) 
        print(5)
        
    def append_digit6(self):
        self.currentRegisterStr = self.currentRegisterStr + '6'        
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, self.currentRegisterStr)
        self.entFlag = False
        print(self.currentRegisterStr) 
        print(6)
        
    def append_digit7(self):
        self.currentRegisterStr = self.currentRegisterStr + '7'        
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, self.currentRegisterStr)
        self.entFlag = False
        print(self.currentRegisterStr) 
        print(7)    
        
    def append_digit8(self):
        self.currentRegisterStr = self.currentRegisterStr + '8'        
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, self.currentRegisterStr)    
        self.entFlag = False
        print(self.currentRegisterStr) 
        print(8)
        
    def append_digit9(self):
        self.currentRegisterStr = self.currentRegisterStr + '9'        
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, self.currentRegisterStr)
        self.entFlag = False
        print(self.currentRegisterStr) 
        print(9)
    def append_minsgn(self):
        self.currentRegisterStr = self.currentRegisterStr + '-'        
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, self.currentRegisterStr)    
        self.entFlag = False
        print(self.currentRegisterStr) 
        print('-')
        
    def append_dec(self):
        self.currentRegisterStr = self.currentRegisterStr + '.'        
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, self.currentRegisterStr)
        self.entFlag = False
        print(self.currentRegisterStr) 
        print('.')


    # doing operations and functions ------------------------------------------
    def do_add(self):
        # check for entered button
        if not self.entFlag:
            self.arithmeticError()
            return
        # add variables entered together
        self.resultVariable = self.operandTwo + self.currentVariable
        # log action to history 
        self.history.see(tk.END)
        # clear register before transfering result there
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, str(self.resultVariable))
        self.history.insert(tk.END, 'SUM  ' + str(self.resultVariable) + '\n')
        # set up for chain operation
        ActionFunctions.do_enterReg(self)
        print("adding")
        print("sum is {}".format(self.resultVariable))
        
    def do_subt(self):
        # check for entered button
        if not self.entFlag:
            self.arithmeticError()
            return
        # subtract variables entered 
        self.resultVariable = self.operandTwo - self.currentVariable
        # log action to history 
        self.history.see(tk.END)
        # clear register before transfering result there
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, str(self.resultVariable))
        self.history.insert(tk.END, 'DIFF  ' + str(self.resultVariable) + '\n')
        # set up for chain operation
        ActionFunctions.do_enterReg(self)

        print("subtracting")
        print("difference is {}".format(self.resultVariable))
        
    def do_mult(self):
        # check for entered button
        if not self.entFlag:
            self.arithmeticError()
            return
        # multiply variables entered 
        self.resultVariable = self.operandTwo * self.currentVariable
        # log action to history 
        
        self.history.see(tk.END)
        # clear register before transfering result there
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, str(self.resultVariable))
        self.history.insert(tk.END, 'PROD  ' + str(self.resultVariable) + '\n')
        # set up for chain operation
        ActionFunctions.do_enterReg(self)
        print("multiplying")
        print("product is {}".format(self.resultVariable))
        
    def do_div(self):
        # check for entered button
        if not self.entFlag:
            self.arithmeticError()
            return
        # divide variables entered, second from first         
        try:
            self.resultVariable = self.operandTwo / self.currentVariable
        except:
            self.improperInputError()
            return
        
        # log action to history 
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, str(self.resultVariable))
        self.history.insert(tk.END, 'DIVD  ' + str(self.resultVariable) + '\n')
        # set up for chain operation
        ActionFunctions.do_enterReg(self)

        print("dividing")
        print("dividend is {}".format(self.resultVariable))
        
    def do_enterReg(self):
        self.operandTwo = self.currentVariable
        try:
            self.currentVariable=float(self.inReg.get())
        except:
            self.castError()
            print("the input can't be blank, a '0' is atleast needed")
        ActionFunctions.do_clrCurRegr(self)
        # log action to history 
        self.history.insert(tk.END, 'ENTERED  ' + str(self.currentVariable) + '\n')
        self.history.see(tk.END)
        self.entFlag = True
        self.inReg.focus()
        print('current Register: ' + self.currentRegisterStr)
        print('current Variable: ' + str(self.currentVariable))
        print("Entered current register into current variable and clear current register")
        print('Operand 2 Variable: ' + str(self.operandTwo))
        
    def do_xpowy(self):
        # check for entered button
        if not self.entFlag:
            self.arithmeticError()
            return
        self.resultVariable = (self.operandTwo)**(self.currentVariable)
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, str(self.resultVariable))
        self.history.insert(tk.END, 'x^y  ' + str(self.resultVariable) + '\n')
        self.history.see(tk.END)
        # set up for chain operation
        ActionFunctions.do_enterReg(self)

        # do something else to (x)
        print('x^y')
        print("y power of x is {}".format(self.resultVariable))
        
    def do_sqrt(self):
        # check for entered button
        if not self.entFlag:
            self.arithmeticError()
            return
        # calculate sqrt(x)
        self.resultVariable = math.sqrt(self.currentVariable)
                # log action to history 
        
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, str(self.resultVariable))
        self.history.insert(tk.END, 'SQRT  ' + str(self.resultVariable) + '\n')
        self.history.see(tk.END)
        # set up for chain operation
        ActionFunctions.do_enterReg(self)

        print("square of x is {}".format(self.resultVariable))
        print('sqrt')
        
    def do_invert(self):
        # check for entered button
        if not self.entFlag:
            self.arithmeticError()
            return
        # calculate square of (x)
        self.resultVariable = 1/self.currentVariable
        # log action to history 
        
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, str(self.resultVariable))
        self.history.insert(tk.END, 'INVERSE  ' + str(self.resultVariable) + '\n')
        self.history.see(tk.END)
        # set up for chain operation
        ActionFunctions.do_enterReg(self)

        print("inverse of x is {}".format(self.resultVariable))
        print('inverse')
        print('inverse of x')
        # calculate inverse (x)
        print('inverted x')
    
    def do_power2(self):
        # check for entered button
        if not self.entFlag:
            self.arithmeticError()
            return
        # calculate square of (x)
        self.resultVariable = self.currentVariable**2
                # log action to history 
        
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, str(self.resultVariable))
        self.history.insert(tk.END, 'POWER2  ' + str(self.resultVariable) + '\n')
        self.history.see(tk.END)
        # set up for chain operation
        ActionFunctions.do_enterReg(self)

        print("square of x is {}".format(self.resultVariable))
        print('sqrt')
        print('squared x')
    
    def do_sgn(self):
        # check for entered button
        if not self.entFlag:
            ActionFunctions.do_enterReg(self)
        # do change of sign too (x)
        self.currentVariable = self.currentVariable * -1
        # log action to history 
        
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, str(self.currentVariable))
        self.history.insert(tk.END, ' +/- ' + str(self.currentVariable) + '\n')
        self.history.see(tk.END)
        print("sign changed, x is now {}".format(self.currentVariable))
        print('change of sign')
    
    def do_cos(self):
        # check for entered button
        if not self.entFlag:
            self.arithmeticError()
            return
        # calculate cos(x) (x in radians!!!
        self.resultVariable = math.cos(self.currentVariable)
                # log action to history 
        
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, str(self.resultVariable))
        self.history.insert(tk.END, 'COS ' + str(self.resultVariable) + '\n')
        self.history.see(tk.END)
        # set up for chain operation
        ActionFunctions.do_enterReg(self)

        print("cosine of x is {}".format(self.resultVariable))
        print('cosine')
        
    def do_sin(self):
        # check for entered button
        if not self.entFlag:
            self.arithmeticError()
            return
        # calculate sqrt(x)
        self.resultVariable = math.sin(self.currentVariable)
                # log action to history 
        
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, str(self.resultVariable))
        self.history.insert(tk.END, 'SIN ' + str(self.resultVariable) + '\n')
        self.history.see(tk.END)
        # set up for chain operation
        ActionFunctions.do_enterReg(self)

        print(" sine of x is {}".format(self.resultVariable))
        print('sine')
        
    def do_tan(self):
        # check for entered button
        if not self.entFlag:
            self.arithmeticError()
            return
        # calculate tangent(x)
        self.resultVariable = math.tan(self.currentVariable)
                # log action to history 
        
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, str(self.resultVariable))
        self.history.insert(tk.END, 'TAN  ' + str(self.resultVariable) + '\n')
        self.history.see(tk.END)
        # set up for chain operation
        ActionFunctions.do_enterReg(self)

        print("tangent of x is {}".format(self.resultVariable))
        print('tangent')
        
    def do_acos(self):
        # check for entered button
        if not self.entFlag:
            self.arithmeticError()
            return
        # calculate cos(x) (x in radians!!!
        self.resultVariable = math.acos(self.currentVariable)
                # log action to history 
        
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, str(self.resultVariable))
        self.history.insert(tk.END, 'COS ' + str(self.resultVariable) + '\n')
        self.history.see(tk.END)
        # set up for chain operation
        ActionFunctions.do_enterReg(self)

        print("cosine of x is {}".format(self.resultVariable))
        print('cosine')
        
    def do_asin(self):
        # check for entered button
        if not self.entFlag:
            self.arithmeticError()
            return
        # calculate sqrt(x)
        self.resultVariable = math.asin(self.currentVariable)
                # log action to history 
        
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, str(self.resultVariable))
        self.history.insert(tk.END, 'SIN ' + str(self.resultVariable) + '\n')
        self.history.see(tk.END)
        # set up for chain operation
        ActionFunctions.do_enterReg(self)

        print(" sine of x is {}".format(self.resultVariable))
        print('sine')
        
    def do_atan(self):
        # check for entered button
        if not self.entFlag:
            self.arithmeticError()
            return
        # calculate tangent(x)
        self.resultVariable = math.atan(self.currentVariable)
                # log action to history 
        
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, str(self.resultVariable))
        self.history.insert(tk.END, 'TAN  ' + str(self.resultVariable) + '\n')
        self.history.see(tk.END)
        # set up for chain operation
        ActionFunctions.do_enterReg(self)

        print("tangent of x is {}".format(self.resultVariable))
        print('tangent')
    def do_log10(self):
        # check for entered button
        if not self.entFlag:
            self.arithmeticError()
            return
        # calculate base 10 log(x)
        try:
            self.resultVariable = math.log10(self.currentVariable)
        except:
            self.improperInputError()
            return
        # log action to history 
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, str(self.resultVariable))
        self.history.insert(tk.END, 'LOG10  ' + str(self.resultVariable) + '\n')
        self.history.see(tk.END)
        # set up for chain operation
        ActionFunctions.do_enterReg(self)

        print("log10 of x is {}".format(self.resultVariable))
        print('LOG')
        
    def do_ln(self):
        # check for entered button
        if not self.entFlag:
            self.arithmeticError()
            return
        # calculate natural log(x)
        try:
            self.resultVariable = math.log(self.currentVariable)
        except:
            self.improperInputError()
            return
        
        # log action to history 
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, str(self.resultVariable))
        self.history.insert(tk.END, 'LN  ' + str(self.resultVariable) + '\n')
        self.history.see(tk.END)
        # set up for chain operation
        ActionFunctions.do_enterReg(self)

        print("ln of x is {}".format(self.resultVariable))
        print('ln')
        
    def get_pi(self):
        # get constant pi
        self.currentVariable = math.pi
        # log action to history 
        
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, str(self.currentVariable))
        self.history.insert(tk.END, ' PI ' + str(self.currentVariable) + '\n')
        self.history.see(tk.END)
        self.entFlag = True
        self.inReg.focus()
        print("PI is {}".format(self.currentVariable))
        print('pi ')
        
    def do_exp(self):
        # check for entered button
        if not self.entFlag:
            self.arithmeticError()
            return
        # calculate exp(x)
        self.resultVariable = math.exp(self.currentVariable)
                # log action to history 
        
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, str(self.resultVariable))
        self.history.insert(tk.END, 'EXP  ' + str(self.resultVariable) + '\n')
        self.history.see(tk.END)
        # set up for chain operation
        ActionFunctions.do_enterReg(self)

        print("exp of x is {}".format(self.resultVariable))
        print('exp()')
        
    def get_e(self):
        # get constant e
        self.currentVariable = math.e
        # log action to history 
        
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, str(self.currentVariable))
        self.history.insert(tk.END, ' e is ' + str(self.currentVariable) + '\n')
        self.history.see(tk.END)
        self.entFlag = True
        self.inReg.focus()
        print("e is {}".format(self.currentVariable))
        print(' e ')
        
    def get_phi(self):
        # calculate PHI - golden ratio
        self.currentVariable = (1 + sqrt(5))/2
        # log action to history 
        
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, str(self.currentVariable))
        self.history.insert(tk.END, ' PHI is ' + str(self.currentVariable) + '\n')
        self.history.see(tk.END)
        self.entFlag = True
        self.inReg.focus()
        print("golden ratio (PHI) is {}".format(self.currentVariable))
        print(" phi ")
        
    def do_deg2rad(self):
        # check for entered button
        if not self.entFlag:
            self.arithmeticError()
            return
        # convert degrees in x to radians (x)
        self.resultVariable = math.radians(self.currentVariable)
                # log action to history 
        
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, str(self.resultVariable))
        self.history.insert(tk.END, 'DEG2RAD  ' + str(self.resultVariable) + '\n')
        self.history.see(tk.END)
        # set up for chain operation
        ActionFunctions.do_enterReg(self)

        print("Deg to Radians of x is {}".format(self.resultVariable))
        print('DEG2RAD')
    
    def do_blank(self):
        # check for entered button
        if not self.entFlag:
            self.arithmeticError()
            return
        self.history.insert(tk.END, 'NOP  \n')
        self.history.see(tk.END)
        # do something else to (x)
        print('unused key')
        
    def do_note(self):
        # check for entered button
        # do something else to (x)
        self.underConstruction()
        print('note function')
    
    def do_clr_notes(self, scr_notes):
        # clear the calculation history
        scr_notes.delete(1.0,tk.END)
        #self.history.insert(tk.END, 'CLEAR HISTORY\n')
        scr_notes.see(tk.END)
        print('cleared the notes pad')
        
    def do_prt_notes(self, scr_notes):
        print("\n Notes:\n")
        print(scr_notes.get(1.0, tk.END) + '\n')  # to Console
        self.history.insert(tk.END, 'PRINT NOTES \n')
        self.history.see(tk.END)
        self.notesToDialog()  # and show in a dialog
        
    def do_log_notes(self):
        self.history.insert(tk.END, self.scr_notes.get(1.0, tk.END) + '\n')
        self.history.see(tk.END)
        
    def do_save_notes(self):
        notesFile = 'CalcNotes' + '.note'
        notesFolder = './Notes/'
        if not path.exists(notesFolder):
            makedirs(notesFolder, exist_ok = True)
        openedFile = open(notesFolder + notesFile,"w")
        openedFile.write(self.scr_notes.get(1.0, tk.END) + '\n')
        openedFile.close()
        self.history.insert(tk.END, 'SAVED NOTES \n')
        self.history.see(tk.END)
        print("save finished")
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