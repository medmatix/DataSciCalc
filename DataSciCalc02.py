#!/usr/bin/python3                   ## linux shell script directive
# -*- coding: utf-8 -*-              ## default character set selection

'''

DataSciCalc_oldest, Main Program Module

Created on Sep 5, 2018
@version: 0.17
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
import sys as sys
import time
from datetime import datetime
import math

# other module imports
from ActionFunctions import ActionFunctions as af
from InputFunctions import InputFunctions as infn

# ~~~ End import section ~~~ =========================


# ====================================================
# GlobalVariables and Constants
# ====================================================

# module level  GLOBALS 
inxRegStr = ''
inLRegStr = []
x = 0.0
y = 0.0
L = []
resVar = 0.0
xFlag = False
Lflag = False
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


        self.inxRegStr = ''
        self.inLRegStr = []
        self.x = 0.0
        self.y = 0.0
        self.L = [0]
        self.resVar = 0.0
        self.xFlag = xFlag
        self.Lflag = Lflag   
        
        # Create instance
        self.win = tk.Tk()
           
        # Add a title
        self.win.title("Data Science Calculator")
        # Add a icon
        if not sys.platform.startswith('linux'):
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
        mBox.showinfo('About DataSciCalc_oldest', 'A Data Science Calculator\n\n (c) David A York, 2018\n http:crunches-data.appspot.com \nVersion: 0.2, development version 0.125 \nlicense: MIT/X-Windows')

    # catch trying to cast a blank to a number
    def castError(self):
        mBox.showwarning(title= "Ooops!!!", message="The Input field can't be blank or non-mumeric \na number should be entered first, then ENTER.\n\nREVERSE POLISH Notation (RPN) means: enter all numbers, THEN choose an operation.The result is always brought forward as follow-up input in case needed\nOperations can be chained by just entering next input.")
                         
    def listError(self):
        mBox.showwarning(title= "Ooops!!!", message="There is something wrong with the way the list has been entered!!.")
    
    def improperInputError(self):
        mBox.showerror(title= "Ooops!!!", message="Improper Operand, did you try to take a log of a negative or to divide by zero, etc.")
    
    def arithmeticError(self):
        mBox.showerror(title= "Ooops!!!", message="you need to enter a value before selecting an operation")
        
    def underConstruction(self):
        mBox.showinfo(title= "Men at Work!!", message="This function has not been implemented yet, \nsorrrrrrry - see next version :)")
        
    # -- make history display dialog and print 
    def historyToDialog(self):
        mBox._show(title="History", message=self.history.get(1.0, tk.END), _icon="", _type="")
    
    def notesToDialog(self):
        mBox._show(title="Notes", message=self.scr_notes.get(1.0, tk.END), _icon='', _type="")
        
    def displayList(self):
        mBox._show(title= "Data List", message="List = " + self.L.__str__(), _icon='', _type="")
        
    def displayxy(self):
        mBox._show(title= "Current x and y", message="x = " + str(self.x) + " y = " + str(self.y), _icon='', _type="")   
            
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
        
        # Adding a Entry widget for x input
        ttk.Label(self.display, text="  x (ANS)").grid(column=0, row=0, padx=4, pady=4,sticky='W')
        self.inxStr = ttk.Entry(self.display, width=68, text='x')
        self.inxStr.grid(column=1, row=0, padx=4, pady=4,sticky='W')
        
        # Show gurrent y value as Label
        ttk.Label(self.display, text="  y   = ").grid(column=0, row=1, padx=4, pady=4,sticky='W')
        self.yValStr = ttk.Label(self.display, width=68, text=str(self.y))
        self.yValStr.grid(column=1, row=1, padx=4, pady=4,sticky='W')
          
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
        
        self.action_xtoList = ttk.Button(self.inputAction, text="APPEND x", command=lambda: af.do_appendx(self))
        self.action_xtoList.grid(column=4, row=0, padx=4, pady=6)

        # Populate inKeys frame with the digit input keys (buttons)
        # Adding digit entry buttons 1 to 3
        
        self.action1 = ttk.Button(self.inKeys, text=" 1 ", takefocus=False, command=lambda: af.append_digit1(self))
        self.action1.grid(column=0, row=0, padx=4, pady=2)

        self.action2 = ttk.Button(self.inKeys, text=" 2 ", takefocus=False, command=lambda: af.append_digit2(self))
        self.action2.grid(column=1, row=0, padx=4, pady=2)
        
        self.action3 = ttk.Button(self.inKeys, text=" 3 ", takefocus=False, command=lambda: af.append_digit3(self))
        self.action3.grid(column=2, row=0, padx=4, pady=2)
        # Adding digit entry buttons 1 to 3
        self.action4 = ttk.Button(self.inKeys, text=" 4 ", takefocus=False, command=lambda: af.append_digit4(self))
        self.action4.grid(column=0, row=2, padx=4, pady=2)

        self.action5 = ttk.Button(self.inKeys, text=" 5 ", takefocus=False, command=lambda: af.append_digit5(self))
        self.action5.grid(column=1, row=2, padx=4, pady=2)
        
        self.action6 = ttk.Button(self.inKeys, text=" 6 ", takefocus=False, command=lambda: af.append_digit6(self))
        self.action6.grid(column=2, row=2, padx=4, pady=2)
        # Adding digit entry buttons 1 to 3
        self.action7 = ttk.Button(self.inKeys, text=" 7 ", takefocus=False, command=lambda: af.append_digit7(self))
        self.action7.grid(column=0, row=4, padx=4, pady=2)

        self.action8 = ttk.Button(self.inKeys, text=" 8 ", takefocus=False, command=lambda: af.append_digit8(self))
        self.action8.grid(column=1, row=4, padx=4, pady=2)
        
        self.action9 = ttk.Button(self.inKeys, text=" 9 ", takefocus=False, command=lambda: af.append_digit9(self))
        self.action9.grid(column=2, row=4, padx=4, pady=2)
        
        self.action_pi = ttk.Button(self.inKeys, text=" \u03C0 ", takefocus=False, command=lambda: af.get_pi(self))
        self.action_pi.grid(column=0, row=6, padx=4, pady=2)
        
        self.action0 = ttk.Button(self.inKeys, text=" 0 ", takefocus=False, command=lambda: af.append_digit0(self))
        self.action0.grid(column=1, row=6, padx=4, pady=2)  
        
        self.action_e = ttk.Button(self.inKeys, text=" e ", takefocus=False, command=lambda: af.get_e(self))
        self.action_e.grid(column=2, row=6, padx=4, pady=2)
                
        self.action_pi = ttk.Button(self.inKeys, text=" - ", takefocus=False, command=lambda: af.get_pi(self))
        self.action_pi.grid(column=0, row=7, padx=4, pady=2)
        
        self.actiondec = ttk.Button(self.inKeys, text=" . ", takefocus=False, command=lambda: af.append_dec(self))
        self.actiondec.grid(column=1, row=7, padx=4, pady=2)
        
        self.action_comma = ttk.Button(self.inKeys, text=" , ", takefocus=False, command=lambda: af.append_comma(self))
        self.action_comma.grid(column=2, row=7, padx=4, pady=2)
        

        # =====================================================================
        # Populate function keys frame 
        # =====================================================================
        
        # for x,y functions ===================================================
    
        self.xyFunctKeys = ttk.LabelFrame(tab1, text=' x,y Function Keys ')
        self.xyFunctKeys.grid(column=0, row=18, padx=8, pady=8)
        
        self.action_add = ttk.Button(self.xyFunctKeys, text=" y + x ", command=lambda: af.do_add(self))
        self.action_add.grid(column=0, row=0, padx=4, pady=6)

        self.action_subt = ttk.Button(self.xyFunctKeys, text=" y - x ", command=lambda: af.do_subt(self))
        self.action_subt.grid(column=1, row=0, padx=4, pady=6)
        
        self.action_mult = ttk.Button(self.xyFunctKeys, text=" y * x ", command=lambda: af.do_mult(self))
        self.action_mult.grid(column=2, row=0, padx=4, pady=6)
        
        self.action_div = ttk.Button(self.xyFunctKeys, text=" y / x ", command=lambda: af.do_div(self))
        self.action_div.grid(column=3, row=0, padx=4, pady=6)
        
        self.action_div = ttk.Button(self.xyFunctKeys, text=" y \u2194 x ", command=lambda: af.do_switchxy(self))
        self.action_div.grid(column=0, row=1, padx=4, pady=6)
                    
        self.action_sgn = ttk.Button(self.xyFunctKeys, text="+/-", command=lambda: af.do_sgn(self))
        self.action_sgn.grid(column=1, row=1, padx=4, pady=6)
        
        self.action_inverse = ttk.Button(self.xyFunctKeys, text=" 1/x ", command=lambda: af.do_invert(self))
        self.action_inverse.grid(column=2, row=1, padx=4, pady=6)
        
        self.action_power2 = ttk.Button(self.xyFunctKeys, text=" x\u00B2 ", command=lambda: af.do_power2(self))
        self.action_power2.grid(column=3, row=1, padx=4, pady=6)

        self.action_xpowy = ttk.Button(self.xyFunctKeys, text=" x\u207F ", command=lambda: af.do_xpowy(self))
        self.action_xpowy.grid(column=0, row=2, padx=4, pady=6)

        self.action_sqrt = ttk.Button(self.xyFunctKeys, text=" \u221Ax", command=lambda: af.do_sqrt(self))
        self.action_sqrt.grid(column=1, row=2, padx=4, pady=6)
        
        self.action_cos = ttk.Button(self.xyFunctKeys, text="cos x", command=lambda: af.do_cos(self))
        self.action_cos.grid(column=2, row=2, padx=4, pady=6)
        
        self.action_sin = ttk.Button(self.xyFunctKeys, text="sin s", command=lambda: af.do_sin(self))
        self.action_sin.grid(column=3, row=2, padx=4, pady=6)
        
        self.action_tan = ttk.Button(self.xyFunctKeys, text="tan x", command=lambda: af.do_tan(self))
        self.action_tan.grid(column=0, row=3, padx=4, pady=6)
        
        self.action_acos = ttk.Button(self.xyFunctKeys, text="acos x", command=lambda: af.do_acos(self))
        self.action_acos.grid(column=1, row=3, padx=4, pady=6)
        
        self.action_asin = ttk.Button(self.xyFunctKeys, text="asin x", command=lambda: af.do_asin(self))
        self.action_asin.grid(column=2, row=3, padx=4, pady=6)
        
        self.action_atan = ttk.Button(self.xyFunctKeys, text="atan x", command=lambda: af.do_atan(self))
        self.action_atan.grid(column=3, row=3, padx=4, pady=6)
        
        self.action_log10 = ttk.Button(self.xyFunctKeys, text=" log10 x", command=lambda: af.do_log10(self))
        self.action_log10.grid(column=0, row=4, padx=4, pady=6)
        
        self.action_ln = ttk.Button(self.xyFunctKeys, text=" ln x ", command=lambda: af.do_ln(self))
        self.action_ln.grid(column=1, row=4, padx=4, pady=6)
        
        self.action_exp = ttk.Button(self.xyFunctKeys, text="exp(x)", command=lambda: af.do_exp(self))
        self.action_exp.grid(column=2, row=4, padx=4, pady=6)
        
        self.action_deg2rad = ttk.Button(self.xyFunctKeys, text="deg \u2192 rad", command=lambda: af.do_deg2rad(self))
        self.action_deg2rad.grid(column=3, row=4, padx=4, pady=6)
        
        # List functions stitched on and x,y switched off 
    
        self.xyFunctKeys.forget()
        self.listFunctKeys = ttk.LabelFrame(tab1, text='List Function Keys ')
        self.listFunctKeys.grid(column=0, row=18, padx=8, pady=8)   
           
        self.action_addL = ttk.Button(self.listFunctKeys, text=" L + x ", command=lambda: af.do_addL(self))
        self.action_addL.grid(column=0, row=0, padx=4, pady=6)

        self.action_subtL = ttk.Button(self.listFunctKeys, text=" L - x ", command=lambda: af.do_subtL(self))
        self.action_subtL.grid(column=1, row=0, padx=4, pady=6)
        
        self.action_multL = ttk.Button(self.listFunctKeys, text=" L * x ", command=lambda: af.do_multL(self))
        self.action_multL.grid(column=2, row=0, padx=4, pady=6)
        
        self.action_divL = ttk.Button(self.listFunctKeys, text=" L / x ", command=lambda: af.do_divL(self))
        self.action_divL.grid(column=3, row=0, padx=4, pady=6)
        
        self.action_sumL = ttk.Button(self.listFunctKeys, text=" \u03a3 L " , command=lambda: af.do_sumL(self))
        self.action_sumL.grid(column=0, row=1, padx=4, pady=6)

        self.action_prodL = ttk.Button(self.listFunctKeys, text=" \u03A0 L ", command=lambda: af.do_prodL(self))
        self.action_prodL.grid(column=1, row=1, padx=4, pady=6)
        
        self.action_inverseL = ttk.Button(self.listFunctKeys, text=" 1/L ", command=lambda: af.do_invert(self))
        self.action_inverseL.grid(column=2, row=1, padx=4, pady=6)
        
        self.action_Lpowerx = ttk.Button(self.listFunctKeys, text=" L\u00B2 ", command=lambda: af.do_power2(self))
        self.action_Lpowerx.grid(column=3, row=1, padx=4, pady=6)
        
        self.action_sin = ttk.Button(self.listFunctKeys, text="sin(L)", command=lambda: af.do_sin(self))
        self.action_sin.grid(column=0, row=2, padx=4, pady=6)
        
        self.action_cos = ttk.Button(self.listFunctKeys, text="cos(L)", command=lambda: af.do_cos(self))
        self.action_cos.grid(column=1, row=2, padx=4, pady=6)
        
        self.action_tan = ttk.Button(self.listFunctKeys, text="tan(L)", command=lambda: af.do_tan(self))
        self.action_tan.grid(column=2, row=2, padx=4, pady=6)
        
        self.action_acos = ttk.Button(self.listFunctKeys, text="acos(L)", command=lambda: af.do_acos(self))
        self.action_acos.grid(column=3, row=2, padx=4, pady=6)
        
        self.action_asin = ttk.Button(self.listFunctKeys, text="asin(l)", command=lambda: af.do_asin(self))
        self.action_asin.grid(column=0, row=3, padx=4, pady=6)
        
        self.action_atan = ttk.Button(self.listFunctKeys, text="atan(L)", command=lambda: af.do_atan(self))
        self.action_atan.grid(column=1, row=3, padx=4, pady=6)
        
        self.action_log10L = ttk.Button(self.listFunctKeys, text=" log10 L", command=lambda: af.do_log10(self))
        self.action_log10L.grid(column=2, row=3, padx=4, pady=6)
        
        self.action_10powL = ttk.Button(self.listFunctKeys, text=" 10^L", command=lambda: af.do_log10(self))
        self.action_10powL.grid(column=3, row=3, padx=4, pady=6)
        
        self.action_lnL = ttk.Button(self.listFunctKeys, text=" ln L ", command=lambda: af.do_ln(self))
        self.action_lnL.grid(column=0, row=4, padx=4, pady=6)
        
        self.action_expL = ttk.Button(self.listFunctKeys, text="exp(L)", command=lambda: af.do_exp(self))
        self.action_expL.grid(column=1, row=4, padx=4, pady=6)
        
        self.action_xroot = ttk.Button(self.listFunctKeys, text="\u207F\u221AL", command=lambda: af.do_exp(self))
        self.action_xroot.grid(column=2, row=4, padx=4, pady=6)
        
        self.action_Lpowx = ttk.Button(self.listFunctKeys, text="L\u207F", command=lambda: af.do_exp(self))
        self.action_Lpowx.grid(column=3, row=4, padx=4, pady=6)
        
        self.action_xchL = ttk.Button(self.listFunctKeys, text="x \u2194 L", command=lambda: af.do_blank(self))
        self.action_xchL.grid(column=0, row=5, padx=4, pady=6)
        
        self.action_deg2rad = ttk.Button(self.listFunctKeys, text="deg \u2192 rad", command=lambda: af.do_deg2rad(self))
        self.action_deg2rad.grid(column=1, row=5, padx=4, pady=6)
        
        self.action_sgn = ttk.Button(self.listFunctKeys, text=" +/- ", command=lambda: af.do_sgn(self))
        self.action_sgn.grid(column=2, row=5, padx=4, pady=6)
        
        self.action_blank = ttk.Button(self.listFunctKeys, text="  ", command=lambda: af.do_blank(self))
        self.action_blank.grid(column=3, row=5, padx=4, pady=6)
        
        self.listFunctKeys.grid_forget()   
            
        
        # Creating a container frame to hold tab2 widgets ============================
        self.notes = ttk.LabelFrame(tab2, text=' Notes ')
        self.notes.grid(column=0, row=0, padx=8, pady=4, sticky='W')
        
        self.notesctl = ttk.LabelFrame(self.notes)
        self.notesctl.grid(column=0, row=0, padx=8, pady=4, sticky='W')
        
        scrolW1  = 53; scrolH1  =  20
        self.scr_notes = scrolledtext.ScrolledText(self.notes, width=scrolW1, height=scrolH1, wrap=tk.WORD)
        self.scr_notes.grid(column=0, row=6, padx=4, pady=4, sticky='WE', columnspan=3)
        
        self.action_clrnotes = ttk.Button(self.notesctl, text="CLEAR", command=lambda: af.do_clr_notes(self, self.scr_notes))
        self.action_clrnotes.grid(column=0, row=0, padx=4, pady=6)
        
        self.action_prtnotes = ttk.Button(self.notesctl, text="PRINT", command=lambda: af.do_prt_notes(self, self.scr_notes))
        self.action_prtnotes.grid(column=1, row=0, padx=4, pady=6)
        
        self.action_lognotes = ttk.Button(self.notesctl, text="LOG IT", command=lambda: af.do_log_notes(self))
        self.action_lognotes.grid(column=2, row=0, padx=4, pady=6)
        self.action_savenotes = ttk.Button(self.notesctl, text="SAVE", command=lambda: af.do_save_note(self))
        self.action_savenotes.grid(column=3, row=0, padx=4, pady=6)
        self.action_loadnotes = ttk.Button(self.notesctl, text="LOAD", command=lambda: af.do_load_note(self))
        self.action_loadnotes.grid(column=4, row=0, padx=4, pady=6)
        
        self.calcHistory = ttk.LabelFrame(tab2, text=' History ')
        self.calcHistory.grid(column=0, row=30, padx=8, pady=4, sticky='W')
        
        self.historyctl = ttk.LabelFrame(self.calcHistory)
        self.historyctl.grid(column=0, row=0, padx=8, pady=4, sticky='W')
        
        # history display field (not used
        scrolW1  = 53; scrolH1  =  4
        self.history = scrolledtext.ScrolledText(self.calcHistory, width=scrolW1, height=scrolH1, wrap=tk.WORD)
        self.history.grid(column=0, row=6, padx=4, pady=4, sticky='WE', columnspan=3)

        self.action_clrhistory = ttk.Button(self.historyctl, text="CLEAR", command=lambda: af.do_clr_history(self, self.history))
        self.action_clrhistory.grid(column=0, row=0, padx=4, pady=6)
        
        self.action_prthistory = ttk.Button(self.historyctl, text="PRINT", command=lambda: af.do_prt_history(self, self.history))
        self.action_prthistory.grid(column=1, row=0, padx=4, pady=6)
        
        self.action_loghistory = ttk.Button(self.historyctl, text="LOG IT", command=lambda: af.do_log_history(self))
        self.action_loghistory.grid(column=2, row=0, padx=4, pady=6)
        
        self.action_savehistory = ttk.Button(self.historyctl, text="SAVE", command=lambda: af.do_save_history(self))
        self.action_savehistory.grid(column=3, row=0, padx=4, pady=6)
        
        self.action_savehistory = ttk.Button(self.historyctl, text=" ", command=lambda: af.do_blank(self))
        self.action_savehistory.grid(column=4, row=0, padx=4, pady=6)
        
        
        
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
        self.statsctl = ttk.LabelFrame(self.statistics, text='Dataset')
        self.statsctl.grid(column=0, row=0, padx=8, pady=4, sticky='W')
          
        self.get_Dataset = ttk.Button(self.statsctl, text="Select", command=lambda: af.do_blank(self))
        self.get_Dataset.grid(column=0, row=0, padx=4, pady=4)

        self.prt_Dataset = ttk.Button(self.statsctl, text=" Print ", command=lambda: af.do_blank(self))
        self.prt_Dataset.grid(column=1, row=0, padx=4, pady=4)
        
        self.grph_Dataset = ttk.Button(self.statsctl, text="  Graph  ", command=lambda: af.do_blank(self))
        self.grph_Dataset.grid(column=2, row=0, padx=4, pady=4)
        
        self.save_Dataset = ttk.Button(self.statsctl, text="Save", command=lambda: af.do_blank(self))
        self.save_Dataset.grid(column=3, row=0, padx=4, pady=6)
        
        self.funct_Dataset = ttk.Button(self.statsctl, text="Analyze", command=lambda: af.do_blank(self))
        self.funct_Dataset.grid(column=4, row=0, padx=4, pady=6)
        
        ttk.Label(self.statistics, text="    Statistics:  this application functionality has not yet been implemented ..........        ", foreground='red').grid(column=0, row=35, sticky='W')
       
        
        
        # Creating a container frame to hold tab5 graphing widgets 
        self.graphical = ttk.LabelFrame(tab5, text=' Graphical Output ')
        self.graphical.grid(column=0, row=0, padx=8, pady=4)
         
        # Adding a graphic window (canvas widget)
        gw = Canvas(self.graphical, width=415, height=550)
               
        gw.create_rectangle(20, 20, 300, 200, fill="blue") 
        gw.create_line(20, 190, 290, 20, fill="red", dash=(4, 4))
        gw.create_text(160,10, fill='green', font='Calabri',  text="A Nice Fudged Graph")
        gw.create_text(155,120, fill='white', text="Graphics NOT yet implemented")
        gw.create_text(5,100,text="Y")
        gw.create_text(165,206,  text="X")
        #=======================================================================
        # img = ImageTk.PhotoImage(file='D:/git/DataSciCalc/images/DNA-tree-crop2-alpha.gif')
        #=======================================================================
        #=======================================================================
        # gw.create_image(55,130,image=img)
        #=======================================================================
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
        editMenu.add_command(label="Delete")
        editMenu.add_command(label="Clear All", command=lambda: af.do_clrAllRegr(self))
        editMenu.add_command(label="Select")
        editMenu.add_separator()
        editMenu.add_command(label="Enter")
        editMenu.add_command(label="Options")
        menuBar.add_cascade(label="Edit", menu=editMenu)
        
        # Add an View Menu
        viewMenu = Menu(menuBar, tearoff=0)
        viewMenu.add_command(label="Toggle Functions", command=lambda:af.do_toggleList(self))
        viewMenu.add_command(label="List data", command=self.displayList)
        viewMenu.add_command(label="x and y", command=self.displayxy)
        viewMenu.add_separator()
        viewMenu.add_command(label=" ")
        viewMenu.add_command(label=" ")
        menuBar.add_cascade(label="View", menu=viewMenu)
        
        # Add an tools Menu
        toolsMenu = Menu(menuBar, tearoff=0)
        toolsMenu.add_command(label="Math")
        toolsMenu.add_command(label="Descriptive")
        toolsMenu.add_command(label="Inference")
        toolsMenu.add_separator()
        toolsMenu.add_command(label="Models")
        toolsMenu.add_command(label="Plots")
        menuBar.add_cascade(label="Data Tools", menu=toolsMenu)

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