#!/usr/bin/python3                   ## linux shell script directive
# -*- coding: utf-8 -*-              ## default character set selection

'''

DataSciCalc, Main Program Module
@summary: This is a data science tool on a desktop calculator theme.

Created on Sep 5, 2018
@version: 0.25  
@author: David A York
@ copyright: 2018
@license: MIT, https://opensource.org/licenses/MIT
@acknowledgement: Farrell, D 2016 DataExplore: An Application for General Data Analysis in Research and Education. Journal of Open Research Software, 4: e9, DOI: http://dx.doi.org/10.5334/jors.94

'''

#======================================================
# imports
#======================================================
# standard library imports
    # tcl/tk imports
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import Canvas
from tkinter import messagebox as mBox
from tkinter import simpledialog
from tkinter import *
    # non-tk/gui imports
from os import path, makedirs
import sys as sys
import time
from datetime import datetime
import math
import numpy as np
import pandas as pd
from pandastable import Table
from scipy import stats

from munging import Munging as mg

# custom module imports
from ActionFunctions import ActionFunctions as af
from Tooltips import createToolTip, ToolTip as tip
from mbox import MessageBox
# ~~~ End import section ~~~ =========================


# ====================================================
# GlobalVariables and Constants
# ====================================================

# module level  GLOBALS 
inxRegStr = ''
inLRegStr = []
x = 0.0
y = 0.0
L = list()
resVar = 0.0
xFlag = False
Lflag = False
logHistoryName = "historyLog"
dfT = pd.DataFrame()
S1 = pd.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)
S2 = pd.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)
arry = np.array(np.arange(10))
active_Dataset = None


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
        self.x = x
        self.y = y
        self.L = L
        self.resVar = resVar
        self.xFlag = xFlag
        self.Lflag = Lflag  
        self.active_Dataset = str(None)
        self.arry = arry
        self.dfT = dfT
        self.S1 = S1
        self.S2 = S2 
        
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
        
    # ##############################################################
    # -- make an messages and messageBoxes for GUI help and errors
    # ##############################################################
    
    def info(self):
        mBox.showinfo('About DataSciCalc', 'A Data Science Calculator\n  "Doing data science in a calculator paradigm"\n\n \u00A9 2018,David A York\nhttp://crunches-data.appspot.com\n\nVersion: 0.3, development version 0.25 \nDataSciCalc Repository:     https://medmatix.github.io/DataSciCalc/\nlicense: MIT/X-Windows')
    
    def miscMessage(self, mTitle, strMessage):
        mBox.showinfo(mTitle, strMessage)
    
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
        mBox.showinfo("Men at Work!!", message="This function has not been implemented yet, \nsorrrrrrry - see next version :)")
        
    # -- make history display dialog and print 
    def historyToDialog(self):
        mBox._show(title="History", message=self.history.get(1.0, tk.END), _icon="", _type="")
    
    def notesToDialog(self):
        mBox._show(title="Notes", message=self.scr_notes.get(1.0, tk.END), _icon='', _type="")
        
    def displayL(self):
        mBox._show(title= "Data List", message="List = " + self.L.__str__(), _icon='', _type="")
    
    def displayArray(self):
        mBox._show(title= "Data List", message="Array = " + self.arry.__str__(), _icon='', _type="")
    
    def displaydfT(self):
        mBox._show(title= "Data Table", message="Table = \n" + self.dfT.__str__(), _icon='', _type="")
         
    def displayS(self):
        mBox._show(title= "Data Series", message="Series = \n" + self.S.__str__(), _icon='', _type="")
        
    def displayxy(self):
        mBox._show(title= "Current x and y", message="x = " + str(self.x) + " y = " + str(self.y), _icon='', _type="")   
    
    # get input from user
    def get1Answer(self, dquestion):
        answer = simpledialog.askstring("Input", dquestion, parent=self.win)
        if answer is not None:
            return answer
        else:
            print("No Value enterd")
            return 0
                  
    # #########################################################       
    # -- GUI widget construction
    # ########################################################
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
        # Associated tool tip
        inxStrDescr = 'Enter an x and press <<ENTER x>> or <<APPEND x>>,\n any previous x becomes y'
        createToolTip(self.inxStr, inxStrDescr)
        
        # Show current y value as Label
        ttk.Label(self.display, text="  y   = ").grid(column=0, row=1, padx=4, pady=4,sticky='W')
        self.yValStr = ttk.Label(self.display, width=68, text=str(self.y))
        self.yValStr.grid(column=1, row=1, padx=4, pady=4,sticky='W')
        
          
        # Scrolling input field for L or y entry ( L is list of sequence entered, y is single number entered:
        # Using a scrolled Text control for List entry
        scrolW1  = 30; scrolH1  =  2
        ttk.Label(self.display, text="List").grid(column=0, row=2, padx=4, pady=4,sticky='W')
        self.inLStr = scrolledtext.ScrolledText(self.display, width=scrolW1, height=scrolH1, wrap=tk.WORD)
        self.inLStr.grid(column=1, row=2, padx=4, pady=4, sticky='WE', columnspan=3)
        # Associated tool tip
        inLStrDescr = 'Enter a comma separated list of values and press <<ENTER L>>'
        createToolTip(self.inLStr, inLStrDescr)
        
        # ################################
        # House keeping function buttons
        # ################################
        
        self.clrx = ttk.Button(self.inputAction, text=" CLR x ", command=lambda: af.do_clrx(self))
        self.clrx.grid(column=0, row=0, padx=4, pady=4)
        # Associated tool tip
        clrxDescr = 'CLEARS the x currently in display box,\n BUT not any x already entered.\n To Clear Internal Variables go to Edit<Clear All>'
        createToolTip(self.clrx, clrxDescr)

        self.clrL = ttk.Button(self.inputAction, text=" CLR L ", command=lambda: af.do_clrL(self))
        self.clrL.grid(column=1, row=0, padx=4, pady=4)
        # Associated tool tip
        clrLDescr = 'CLEARS the list L currently in display box,\n BUT not any L already entered.\n To Clear Internal Variables go to Edit<Clear All>'
        createToolTip(self.clrL, clrLDescr)
        
        self.toList = ttk.Button(self.inputAction, text="  ENTER L  ", command=lambda: af.do_enterL(self))
        self.toList.grid(column=2, row=0, padx=4, pady=4)
        # Associated tool tip
        toListDescr = 'MOVES string representation of above "List"\n into a the list of floats to act on'
        createToolTip(self.toList, toListDescr)
        
        self.action_toxVar = ttk.Button(self.inputAction, text="ENTER x", command=lambda: af.do_enterx(self))
        self.action_toxVar.grid(column=3, row=0, padx=4, pady=6)
        # Associated tool tip
        toxVarDescr = 'MOVES displayed x above\n into a floats variable x'
        createToolTip(self.action_toxVar, toxVarDescr)
        
        self.action_xtoList = ttk.Button(self.inputAction, text="APPEND x", command=lambda: af.do_appendx(self))
        self.action_xtoList.grid(column=4, row=0, padx=4, pady=6)
        # Associated tool tip
        xtoListDescr = 'APPENDS displayed x above onto a the "List" shown.\n and moves the new list to a list variable.\n"List" must have at least one starting value already'
        createToolTip(self.action_xtoList, xtoListDescr)
        
        # ##########################################################
        # Populate inKeys frame with the digit input keys (buttons)
        #     Adding digit entry buttons 1 to 3
        # ##########################################################
        
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
        
        # Special Digit keys 
        self.action_pi = ttk.Button(self.inKeys, text=" \u03C0 ", takefocus=False, command=lambda: af.get_pi(self))
        self.action_pi.grid(column=0, row=6, padx=4, pady=2)
        # Associated tool tip
        enterPIDescr = 'Enters the python internal PI value into x,\n moving the previous x to y'
        createToolTip(self.action_pi, enterPIDescr)
        
        self.action0 = ttk.Button(self.inKeys, text=" 0 ", takefocus=False, command=lambda: af.append_digit0(self))
        self.action0.grid(column=1, row=6, padx=4, pady=2)  
        
        self.action_e = ttk.Button(self.inKeys, text=" e ", takefocus=False, command=lambda: af.get_e(self))
        self.action_e.grid(column=2, row=6, padx=4, pady=2)# Associated tool tip
        enterEDescr = 'Enters the python internal e (Euler Constant) value/n into x, moving the previous x to y'
        createToolTip(self.action_e, enterEDescr)
                
        self.action_minSgn = ttk.Button(self.inKeys, text=" - ", takefocus=False, command=lambda: af.append_minSgn(self))
        self.action_minSgn.grid(column=0, row=7, padx=4, pady=2)
        
        self.actiondec = ttk.Button(self.inKeys, text=" . ", takefocus=False, command=lambda: af.append_dec(self))
        self.actiondec.grid(column=1, row=7, padx=4, pady=2)
        
        self.action_comma = ttk.Button(self.inKeys, text=" , ", takefocus=False, command=lambda: af.append_comma(self))
        self.action_comma.grid(column=2, row=7, padx=4, pady=2)
        

        '''
        Populate function keys frames 
            * Discrete valued (x,y) functions
            * List Math Functions
            * List Statistics Functions
        '''        
        # ####################################
        # Discrete valued x,y Functions Keys defined
        # ####################################
        
        self.xyFunctKeys = ttk.LabelFrame(tab1, text=' x,y Function Keys ')
        self.xyFunctKeys.grid(column=0, row=18, padx=8, pady=8)
        
        self.action_add = ttk.Button(self.xyFunctKeys, text=" y + x ", command=lambda: af.do_add(self))
        self.action_add.grid(column=0, row=0, padx=4, pady=6)
        # Associated tool tip
        additionDescr = 'Add x and y result to x'
        createToolTip(self.action_add, additionDescr)

        self.action_subt = ttk.Button(self.xyFunctKeys, text=" y - x ", command=lambda: af.do_subt(self))
        self.action_subt.grid(column=1, row=0, padx=4, pady=6)
        # Associated tool tip
        subtractionDescr = 'Subtract x from y result to x'
        createToolTip(self.action_subt, subtractionDescr)
        
        self.action_mult = ttk.Button(self.xyFunctKeys, text=" y * x ", command=lambda: af.do_mult(self))
        self.action_mult.grid(column=2, row=0, padx=4, pady=6)
        # Associated tool tip
        multiplicationDescr = 'Multiply x and y result to x'
        createToolTip(self.action_mult, multiplicationDescr)
        
        self.action_div = ttk.Button(self.xyFunctKeys, text=" y / x ", command=lambda: af.do_div(self))
        self.action_div.grid(column=3, row=0, padx=4, pady=6)
        # Associated tool tip
        divisionDescr = 'Divide x into y result to x'
        createToolTip(self.action_div, divisionDescr)
        
        self.action_switchxy = ttk.Button(self.xyFunctKeys, text=" y \u2194 x ", command=lambda: af.do_switchxy(self))
        self.action_switchxy.grid(column=4, row=0, padx=4, pady=6)
        # Associated tool tip
        switchDescr = 'Switch x and y values internally'
        
        createToolTip(self.action_switchxy, switchDescr)
                    
        self.action_sgn = ttk.Button(self.xyFunctKeys, text="+/-", command=lambda: af.do_sgn(self))
        self.action_sgn.grid(column=0, row=1, padx=4, pady=6)
        # Associated tool tip
        chgSgnDescr = 'Change sign of x in memory echo result to x field.\n NOT necessary to press ENTERx'
        createToolTip(self.action_sgn, chgSgnDescr)
        
        self.action_inverse = ttk.Button(self.xyFunctKeys, text=" 1/x ", command=lambda: af.do_invert(self))
        self.action_inverse.grid(column=1, row=1, padx=4, pady=6)
        # Associated tool tip
        invertXDescr = 'Invert X in memory result to x.'
        createToolTip(self.action_inverse, invertXDescr)
        
        self.action_power2 = ttk.Button(self.xyFunctKeys, text=" x\u00B2 ", command=lambda: af.do_power2(self))
        self.action_power2.grid(column=2, row=1, padx=4, pady=6)
        # Associated tool tip
        squareXDescr = 'Square X in memory result to x.'
        createToolTip(self.action_power2, squareXDescr)
        
        self.action_xpowy = ttk.Button(self.xyFunctKeys, text=" y\u207F ", command=lambda: af.do_xpowy(self))
        self.action_xpowy.grid(column=3, row=1, padx=4, pady=6)
        # Associated tool tip
        xpowyDescr = 'x to power y result to x.\n'
        createToolTip(self.action_xpowy, xpowyDescr)

        self.action_sqrt = ttk.Button(self.xyFunctKeys, text=" \u221Ax", command=lambda: af.do_sqrt(self))
        self.action_sqrt.grid(column=4, row=1, padx=4, pady=6)
        # Associated tool tip
        sqrtDescr = 'Take square root of x result to x.\n'
        createToolTip(self.action_sqrt, sqrtDescr)
        
        self.action_cos = ttk.Button(self.xyFunctKeys, text="cos x", command=lambda: af.do_cos(self))
        self.action_cos.grid(column=0, row=2, padx=4, pady=6)
        # Associated tool tip
        cosDescr = 'Take Cosine of x result to x.\n'
        createToolTip(self.action_cos, cosDescr)
        
        self.action_sin = ttk.Button(self.xyFunctKeys, text="sin x", command=lambda: af.do_sin(self))
        self.action_sin.grid(column=1, row=2, padx=4, pady=6)
        # Associated tool tip
        sinDescr = 'Take Sine of x result to x.\n'
        createToolTip(self.action_sin, sinDescr)
        
        self.action_tan = ttk.Button(self.xyFunctKeys, text="tan x", command=lambda: af.do_tan(self))
        self.action_tan.grid(column=2, row=2, padx=4, pady=6)
        # Associated tool tip
        tanDescr = 'Take tan of x result to x.\n'
        createToolTip(self.action_tan, tanDescr)
        
        self.action_acos = ttk.Button(self.xyFunctKeys, text="acos x", command=lambda: af.do_acos(self))
        self.action_acos.grid(column=3, row=2, padx=4, pady=6)
        # Associated tool tip
        arcCosineDescr = 'Take arcCosine of x result to x.\n'
        createToolTip(self.action_acos, arcCosineDescr)
        
        self.action_asin = ttk.Button(self.xyFunctKeys, text="asin x", command=lambda: af.do_asin(self))
        self.action_asin.grid(column=4, row=2, padx=4, pady=6)
        # Associated tool tip
        arcsinDescr = 'Take arcsine of x result to x.\n'
        createToolTip(self.action_asin, arcsinDescr)
        
        self.action_atan = ttk.Button(self.xyFunctKeys, text="atan x", command=lambda: af.do_atan(self))
        self.action_atan.grid(column=0, row=3, padx=4, pady=6)
        # Associated tool tip
        arctanDescr = 'Take arctan of x result to x.\n'
        createToolTip(self.action_atan, arctanDescr)
        
        self.action_log10 = ttk.Button(self.xyFunctKeys, text=" log10 x", command=lambda: af.do_log10(self))
        self.action_log10.grid(column=1, row=3, padx=4, pady=6)
        # Associated tool tip
        log10Descr = 'Take base 10 log of x result to x.\n'
        createToolTip(self.action_log10, log10Descr)
        
        self.action_ln = ttk.Button(self.xyFunctKeys, text=" ln x ", command=lambda: af.do_ln(self))
        self.action_ln.grid(column=2, row=3, padx=4, pady=6)
        # Associated tool tip
        lnDescr = 'Take natural log of x result to x.\n'
        createToolTip(self.action_ln, lnDescr)
        
        self.action_exp = ttk.Button(self.xyFunctKeys, text="exp(x)", command=lambda: af.do_exp(self))
        self.action_exp.grid(column=3, row=3, padx=4, pady=6)
        # Associated tool tip
        expDescr = 'Take exponent (base e to power) of x result to x.\n'
        createToolTip(self.action_exp, expDescr)
        
        self.action_factorial = ttk.Button(self.xyFunctKeys, text=" x!", command=lambda: af.do_factorial(self))
        self.action_factorial.grid(column=4, row=3, padx=4, pady=6)
        # Associated tool tip
        factorialDescr = 'Take factorial of x result to x.\n'
        createToolTip(self.action_factorial, factorialDescr)
        
        self.action_xrooty = ttk.Button(self.xyFunctKeys, text="\u207F\u221A y ", command=lambda: af.do_blank(self))
        self.action_xrooty.grid(column=0, row=4, padx=4, pady=6)
        # Associated tool tip
        xrootyDescr = 'Take xth root of y, result to x.\n'
        createToolTip(self.action_xrooty, xrootyDescr)
        
        self.action_blank = ttk.Button(self.xyFunctKeys, text="  ", command=lambda: af.do_blank(self))
        self.action_blank.grid(column=1, row=4, padx=4, pady=6)
        # Associated tool tip
        blankDescr = 'Unassigned key'
        createToolTip(self.action_blank, blankDescr)
        
        self.action_blank1 = ttk.Button(self.xyFunctKeys, text="   ", command=lambda: af.do_blank(self))
        self.action_blank1.grid(column=2, row=4, padx=4, pady=6)
        # Associated tool tip
        blankDescr = 'Unassigned key.\n'
        createToolTip(self.action_blank1, blankDescr)
        
        self.action_blank2 = ttk.Button(self.xyFunctKeys, text=" ", command=lambda: af.do_blank(self))
        self.action_blank2.grid(column=3, row=4, padx=4, pady=6)
        # Associated tool tip
        blankDescr = 'Unassigned key'
        createToolTip(self.action_blank2, blankDescr)
        
        # Convert degrees to radians
        self.action_deg2rad = ttk.Button(self.xyFunctKeys, text="deg \u2192 rad", command=lambda: af.do_deg2rad(self))
        self.action_deg2rad.grid(column=4, row=4, padx=4, pady=6)
        # Associated tool tip
        deg2radDescr = 'Convert x from degrees to radians result to x.\n'
        createToolTip(self.action_deg2rad, deg2radDescr)
        
        # #####################################
        # List math functions Keys defined 
        # #####################################
        
        self.listFunctKeys = ttk.LabelFrame(tab1, text='List Function Keys ')
        self.listFunctKeys.grid(column=0, row=18, padx=8, pady=8)
                   
        self.action_addL = ttk.Button(self.listFunctKeys, text=" L + x ", command=lambda: af.do_addL(self))
        self.action_addL.grid(column=0, row=0, padx=4, pady=6)
        # Associated tool tip
        addtoListDescr = 'Add x to L element-wise, result to L'
        createToolTip(self.action_addL, addtoListDescr)  

        self.action_subtL = ttk.Button(self.listFunctKeys, text=" L - x ", command=lambda: af.do_subtL(self))
        self.action_subtL.grid(column=1, row=0, padx=4, pady=6)
        # Associated tool tip
        subtfromListDescr = 'Subtract x from L element-wise, result to L'
        createToolTip(self.action_subtL, subtfromListDescr)
        
        self.action_multL = ttk.Button(self.listFunctKeys, text=" L * x ", command=lambda: af.do_multL(self))
        self.action_multL.grid(column=2, row=0, padx=4, pady=6)
        # Associated tool tip
        multListDescr = 'Multiply L by x element-wise, result to L'
        createToolTip(self.action_multL, multListDescr)
        
        self.action_divL = ttk.Button(self.listFunctKeys, text=" L / x ", command=lambda: af.do_divL(self))
        self.action_divL.grid(column=3, row=0, padx=4, pady=6)
        # Associated tool tip
        divListDescr = 'Divide L by x element-wise, result to L'
        createToolTip(self.action_divL, divListDescr)        
        
        self.action_sumL = ttk.Button(self.listFunctKeys, text=" \u03a3 L " , command=lambda: af.do_sumL(self))
        self.action_sumL.grid(column=0, row=1, padx=4, pady=6)
        # Associated tool tip
        sumListDescr = 'Sum elements of L, result to L'
        createToolTip(self.action_sumL, sumListDescr)  

        self.action_prodL = ttk.Button(self.listFunctKeys, text=" \u03A0 L ", command=lambda: af.do_prodL(self))
        self.action_prodL.grid(column=1, row=1, padx=4, pady=6)
        # Associated tool tip
        prodListDescr = 'Product of elements of L, result to L'
        createToolTip(self.action_prodL, prodListDescr) 
        
        self.action_inverseL = ttk.Button(self.listFunctKeys, text=" 1/L ", command=lambda: af.do_invertL(self))
        self.action_inverseL.grid(column=2, row=1, padx=4, pady=6)
        # Associated tool tip
        invListDescr = 'Invert elements of L, result to L'
        createToolTip(self.action_inverseL, invListDescr) 
        
        self.action_Lpower2 = ttk.Button(self.listFunctKeys, text=" L\u00B2 ", command=lambda: af.do_Lpower2(self))
        self.action_Lpower2.grid(column=3, row=1, padx=4, pady=6)
        # Associated tool tip
        pow2ListDescr = 'Squares of elements of L, result to L'
        createToolTip(self.action_Lpower2, pow2ListDescr) 
        
        
        self.action_Lpowx = ttk.Button(self.listFunctKeys, text="L\u207F", command=lambda: af.do_Lpowx(self))
        self.action_Lpowx.grid(column=0, row=2, padx=4, pady=6)
        # Associated tool tip
        xpowListDescr = 'x powers of elements of L, result to L'
        createToolTip(self.action_Lpowx, xpowListDescr) 
        
        self.action_sqrtL = ttk.Button(self.listFunctKeys, text="\u221AL", command=lambda: af.do_sqrtL(self))
        self.action_sqrtL.grid(column=1, row=2, padx=4, pady=6)
        # Associated tool tip
        sqrtListDescr = 'Square roots of of elements of L, result to L'
        createToolTip(self.action_sqrtL, sqrtListDescr) 
        
        self.action_sinL = ttk.Button(self.listFunctKeys, text="sin(L)", command=lambda: af.do_sinL(self))
        self.action_sinL.grid(column=2, row=2, padx=4, pady=6)
        # Associated tool tip
        sinListDescr = 'Sine of elements of L, result to L'
        createToolTip(self.action_sinL, sinListDescr) 
        
        self.action_cosL = ttk.Button(self.listFunctKeys, text="cos(L)", command=lambda: af.do_cosL(self))
        self.action_cosL.grid(column=3, row=2, padx=4, pady=6)
        # Associated tool tip
        cosListDescr = 'Cosine of elements of L, result to L'
        createToolTip(self.action_cosL, cosListDescr)
        
        self.action_tanL = ttk.Button(self.listFunctKeys, text="tan(L)", command=lambda: af.do_tanL(self))
        self.action_tanL.grid(column=0, row=3, padx=4, pady=6)
        # Associated tool tip
        tanListDescr = 'Tangent of elements of L, result to L'
        createToolTip(self.action_tanL, tanListDescr)
        
        self.action_acosL = ttk.Button(self.listFunctKeys, text="acos(L)", command=lambda: af.do_acosL(self))
        self.action_acosL.grid(column=1, row=3, padx=4, pady=6)
        # Associated tool tip
        acosListDescr = 'AcrCosine of elements of L, result to L'
        createToolTip(self.action_acosL, acosListDescr)
        
        self.action_asinL = ttk.Button(self.listFunctKeys, text="asin(L)", command=lambda: af.do_asinL(self))
        self.action_asinL.grid(column=2, row=3, padx=4, pady=6)
        # Associated tool tip
        asinListDescr = 'arcsine of elements of L, result to L'
        createToolTip(self.action_asinL, asinListDescr)
        
        self.action_atanL = ttk.Button(self.listFunctKeys, text="atan(L)", command=lambda: af.do_atanL(self))
        self.action_atanL.grid(column=3, row=3, padx=4, pady=6)
        # Associated tool tip
        atanListDescr = 'Arctangent of elements of L, result to L'
        createToolTip(self.action_atanL, atanListDescr)
        
        self.action_log10L = ttk.Button(self.listFunctKeys, text=" log10 L", command=lambda: af.do_log10L(self))
        self.action_log10L.grid(column=0, row=4, padx=4, pady=6)
        # Associated tool tip
        log10ListDescr = 'Base 10 log of elements of L, result to L'
        createToolTip(self.action_log10L, log10ListDescr)
        
        self.action_10powL = ttk.Button(self.listFunctKeys, text=" 10^L", command=lambda: af.do_10powL(self))
        self.action_10powL.grid(column=1, row=4, padx=4, pady=6)
        # Associated tool tip
        pow10ListDescr = 'Element-wise Powers of 10 of L, result to L'
        createToolTip(self.action_10powL, pow10ListDescr)
        
        self.action_lnL = ttk.Button(self.listFunctKeys, text=" ln L ", command=lambda: af.do_lnL(self))
        self.action_lnL.grid(column=2, row=4, padx=4, pady=6)
        # Associated tool tip
        lnListDescr = 'Natural log of elements of L, result to L'
        createToolTip(self.action_lnL, lnListDescr)
        
        self.action_expL = ttk.Button(self.listFunctKeys, text="exp(L)", command=lambda: af.do_expL(self))
        self.action_expL.grid(column=3, row=4, padx=4, pady=6)
        # Associated tool tip
        expListDescr = 'Take exponent (base e to power) of elements of L result to L.\n'
        createToolTip(self.action_expL, expListDescr)
        
        
        self.action_xchL = ttk.Button(self.listFunctKeys, text="  ", command=lambda: af.do_blank(self))
        self.action_xchL.grid(column=0, row=5, padx=4, pady=6)
        
        self.action_Ldeg2rad = ttk.Button(self.listFunctKeys, text="deg \u2192 rad", command=lambda: af.do_Ldeg2Lrad(self))
        self.action_Ldeg2rad.grid(column=1, row=5, padx=4, pady=6)
        # Associated tool tip
        deg2radListDescr = 'Convert elements of L from degrees to radians result to L.\n'
        createToolTip(self.action_Ldeg2rad, deg2radListDescr)
        
        self.action_sgnL = ttk.Button(self.listFunctKeys, text=" +/- ", command=lambda: af.do_sgnL(self))
        self.action_sgnL.grid(column=2, row=5, padx=4, pady=6)
        # Associated tool tip
        sgnListDescr = 'Change signs of elements of L, result to L.\n'
        createToolTip(self.action_sgnL, sgnListDescr)
                      
        self.action_LStats = ttk.Button(self.listFunctKeys, text="L Stats", command=lambda: af.do_LStats(self))
        self.action_LStats.grid(column=3, row=5, padx=4, pady=6)
        # Associated tool tip
        LStatsDescr = 'Bring-up keypad for statistics on L.\n'
        createToolTip(self.action_LStats, LStatsDescr)
        
        # #####################################################################
        # List Descriptive (and univariate) Statistics functions Keys defined 
        # #####################################################################
                
        self.listStatsKeys = ttk.LabelFrame(tab1, text=' List Statistics Function Keys ')
        self.listStatsKeys.grid(column=3, row=5, padx=4, pady=6)
        
        self.action_meanL = ttk.Button(self.listStatsKeys, text="mean L", command=lambda: af.do_meanL(self))
        self.action_meanL.grid(column=0, row=0, padx=4, pady=6)
        # Associated tool tip
        meanListDescr = 'Find mean of elements of L, result to x\n'
        createToolTip(self.action_meanL, meanListDescr)

        self.action_medianL = ttk.Button(self.listStatsKeys, text="median L   ", command=lambda: af.do_medianL(self))
        self.action_medianL.grid(column=1, row=0, padx=4, pady=6)
        # Associated tool tip
        medianListDescr = 'Find median value of elements of L, result to x\n'
        createToolTip(self.action_medianL, medianListDescr)
        
        self.action_minL = ttk.Button(self.listStatsKeys, text="min L", command=lambda: af.do_minL(self))
        self.action_minL.grid(column=2, row=0, padx=4, pady=6)
        # Associated tool tip
        minListDescr = 'Find minimum of elements of L, result to x\n'
        createToolTip(self.action_minL, minListDescr)
        
        self.action_maxL = ttk.Button(self.listStatsKeys, text="max L", command=lambda: af.do_maxL(self))
        self.action_maxL.grid(column=3, row=0, padx=4, pady=6)
        # Associated tool tip
        maxListDescr = 'Find maximum of elements of L, result to x\n'
        createToolTip(self.action_maxL, maxListDescr)
        
        self.action_sdevL = ttk.Button(self.listStatsKeys, text="sdev L" , command=lambda: af.do_pstdevL(self))
        self.action_sdevL.grid(column=0, row=1, padx=4, pady=6)
        # Associated tool tip
        sdevListDescr = 'Find population standard deviation of elements of L, result to x\n'
        createToolTip(self.action_sdevL, sdevListDescr)

        self.action_countL = ttk.Button(self.listStatsKeys, text="n of L", command=lambda: af.do_countL(self))
        self.action_countL.grid(column=1, row=1, padx=4, pady=6)
        # Associated tool tip
        countListDescr = 'Find number n of elements in L, result to x\n'
        createToolTip(self.action_countL, countListDescr)
        
        self.action_25thL = ttk.Button(self.listStatsKeys, text="25th L", command=lambda: af.do_quartile1L(self))
        self.action_25thL.grid(column=2, row=1, padx=4, pady=6)
        # Associated tool tip
        Q25thListDescr = 'Find 25th quantile of elements of L, result to x\n'
        createToolTip(self.action_25thL, Q25thListDescr)
        
        self.action_75thL = ttk.Button(self.listStatsKeys, text="75th L", command=lambda: af.do_quartile3L(self))
        self.action_75thL.grid(column=3, row=1, padx=4, pady=6)
        # Associated tool tip
        Q75thListDescr = 'Find 75th quantile of elements of L, result to x\n'
        createToolTip(self.action_75thL, Q75thListDescr)
        
        
        self.action_svTtestL = ttk.Button(self.listStatsKeys, text="t-test L", command=lambda: af.do_svTtestL(self))
        self.action_svTtestL.grid(column=0, row=2, padx=4, pady=6)
        # Associated tool tip
        svTtestListDescr = 'Single Sample t-Test on elements of L, result to x\n H\u2080 mean of L is not different from zero at \u03B1 = 0.05%'
        createToolTip(self.action_svTtestL, svTtestListDescr)
        
        self.action_svZtestL = ttk.Button(self.listStatsKeys, text="z-test L", command=lambda: af.do_svZtestL(self))
        self.action_svZtestL.grid(column=1, row=2, padx=4, pady=6)
        # Associated tool tip
        svZtestListDescr = 'Single Sample z-Test on elements of L, result to x\n H\u2080 mean of L is not different from zero at \u03B1 = 0.05%'
        createToolTip(self.action_svZtestL, svZtestListDescr)
        
        self.action_CI95L = ttk.Button(self.listStatsKeys, text="CI 95%", command=lambda: af.do_CI95L(self))
        self.action_CI95L.grid(column=2, row=2, padx=4, pady=6)
        # Associated tool tip
        CI95ListDescr = 'Calculate a 95% Confidence interval for list mean'
        createToolTip(self.action_CI95L, CI95ListDescr)
        
        self.action_histL = ttk.Button(self.listStatsKeys, text="Histogram", command=lambda: af.do_histL(self))
        self.action_histL.grid(column=3, row=2, padx=4, pady=6)
        # Associated tool tip
        HistListDescr = 'Show sample Frequency Distribution'
        createToolTip(self.action_histL, HistListDescr)
                    
        
        # Now turn off all List Functions Keys
        self.listFunctKeys.grid_forget()
        self.listStatsKeys.grid_forget()
        
        
        # Creating a container frame to hold tab2 widgets ============================
        self.notes = ttk.LabelFrame(tab2, text=' Notes ', width=56)
        self.notes.grid(column=0, row=0, padx=8, pady=4, sticky='W')
        
        self.notesctl = ttk.LabelFrame(self.notes, width=56)
        self.notesctl.grid(column=0, row=0, padx=8, pady=4, sticky='W')
        
        scrolW1  = 56; scrolH1  =  20
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
        
        self.calcHistory = ttk.LabelFrame(tab2, text=' History ', width=56)
        self.calcHistory.grid(column=0, row=30, padx=8, pady=4, sticky='W')
        
        self.historyctl = ttk.LabelFrame(self.calcHistory, width=56)
        self.historyctl.grid(column=0, row=0, padx=8, pady=4, sticky='W')
        
        # history display field part of Notes tab2
        scrolW1  = 56; scrolH1  =  4
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
        self.documentation = ttk.LabelFrame(tab3, text=' The Manual ',width= 56)
        self.documentation.grid(column=0, row=3, padx=8, pady=4, sticky='W')
        
        # the index of the manual
        ttk.Label(self.documentation, text="Manual Sections:").grid(column=0, row=0)
        self.choice = tk.StringVar()
        self.indexChosen = ttk.Combobox(self.documentation, width=65, textvariable=self.choice)
        self.indexChosen['values'] = ('All', 'Overview', 'Introduction', 'Operations', 'Functions', 'References', 'Further Explorations')
        self.indexChosen.current(0)
        self.indexChosen.grid(column=0, row=1)
        
        
        # #######################################################
        # The Manual text                
        # Scrolling Documentation field:
        # #######################################################
        
        ttk.Label(self.documentation, text="Documentation:").grid(column=0, row=5, sticky='W')
        
        # Using a scrolled Text control for review of documentation
        scrolW1  = 56; scrolH1  =  30
        self.manual = scrolledtext.ScrolledText(self.documentation, width=scrolW1, height=scrolH1, wrap=tk.WORD)
        self.manual.grid(column=0, row=6, padx=4, pady=4, sticky='WE', columnspan=3)
        section = "./documentation/all_docs.txt"
        docFile=open(section, 'r')
        self.manual.insert(tk.INSERT, '\n' + docFile.read())
        
        # #########################################################
        # Tab4 Multivariate statistics Analyses iterface code
        #
        # #########################################################
        # Creating a container frame to hold tab4 widgets
        self.statistics = ttk.LabelFrame(tab4, text=' A Statistical Applications Interface ',width=68)
        self.statistics.grid(column=0, row=3, padx=8, pady=4, sticky='W')
        
        
        # Frames for data management keys
        self.statsdata = ttk.LabelFrame(self.statistics, text='Dataset', width=56)
        self.statsdata.grid(padx=8, pady=4, sticky='W')
        
        self.datalabel=ttk.Label(self.statsdata, text="Current Active Dataset:  ").grid(column=0,row = 0,sticky='W')
        self.dataSetStr = ttk.Label(self.statsdata, text=self.active_Dataset)
        self.dataSetStr.grid(column=1, row=0, padx=10, pady=4, sticky='W')
        self.dataSetBtn = ttk.Button(self.statsdata, text="Refresh", command=lambda:af.refresh_DSet(self))
        self.dataSetBtn.grid(column=3, row=0, padx=8, pady=4, sticky='W')   
        self.dataEditBtn = ttk.Button(self.statsdata, text="Edit", command=lambda:af.refresh_DSet(self))
        self.dataEditBtn.grid(column=4, row=0, padx=8, pady=4, sticky='W')                           

        self.statsctl = ttk.LabelFrame(self.statistics,width=56)
        self.statsctl.grid(column=0, row=1, padx=8, pady=4, sticky='W')
         
        self.get_Dataset = ttk.Button(self.statsctl, text="Select", command=lambda:af.do_setActiveDataset(self))
        self.get_Dataset.grid(column=0, row=0, padx=4, pady=4)

        self.prt_Dataset = ttk.Button(self.statsctl, text=" Print ", command=lambda: self.miscMessage("Dataset", "The currently active Dataset is \n{}".format(self.active_Dataset)))
        self.prt_Dataset.grid(column=1, row=0, padx=4, pady=4)
        
        self.grph_Dataset = ttk.Button(self.statsctl, text="  Graph  ", command=lambda: af.do_blank(self))
        self.grph_Dataset.grid(column=2, row=0, padx=4, pady=4)
        
        self.save_Dataset = ttk.Button(self.statsctl, text="Save", command=lambda: af.do_blank(self))
        self.save_Dataset.grid(column=3, row=0, padx=4, pady=6)
        
        self.funct_Dataset = ttk.Button(self.statsctl, text="Load", command=lambda: af.loadData(self, active_Dataset))
        self.funct_Dataset.grid(column=4, row=0, padx=4, pady=6)
        
        # Incomplete Implementation notice #############
        ttk.Label(self.statistics, text="    Statistics: this application functionality has not yet been fully implemented .....        ", foreground='red').grid(column=0, row=35, sticky='W')
       
       
        # ###########################################################
        # Container frame to hold Multivariate Statistics Functions
        # ###########################################################
        
        self.mvStatFunctKeys = ttk.LabelFrame(self.statistics, text=' Multivariate Statistics Function Keys ')
        self.mvStatFunctKeys.grid(column=0, row=6, padx=8, pady=8)
        
        self.action_blank = ttk.Button(self.mvStatFunctKeys, text="   ", command=lambda: af.do_blank(self))
        self.action_blank.grid(column=0, row=0, padx=4, pady=6)
        # Associated tool tip
        additionDescr = 'Not implemented yet'
        createToolTip(self.action_blank, additionDescr)

        self.action_blank0 = ttk.Button(self.mvStatFunctKeys, text="   ", command=lambda: af.do_blank(self))
        self.action_blank0.grid(column=1, row=0, padx=4, pady=6)
        # Associated tool tip
        subtractionDescr = 'Not implemented yet'
        createToolTip(self.action_blank0, subtractionDescr)
        
        self.action_blank1 = ttk.Button(self.mvStatFunctKeys, text="   ", command=lambda: af.do_blank(self))
        self.action_blank1.grid(column=2, row=0, padx=4, pady=6)
        # Associated tool tip
        multiplicationDescr = 'Not implemented yet'
        createToolTip(self.action_blank1, multiplicationDescr)
        
        self.action_blank2 = ttk.Button(self.mvStatFunctKeys, text="   ", command=lambda: af.do_blank(self))
        self.action_blank2.grid(column=3, row=0, padx=4, pady=6)
        # Associated tool tip
        divisionDescr = 'Unassigned key'
        createToolTip(self.action_blank2, divisionDescr)
        
        self.action_blank3 = ttk.Button(self.mvStatFunctKeys, text="   ", command=lambda: af.do_blank(self))
        self.action_blank3.grid(column=4, row=0, padx=4, pady=6)
        # Associated tool tip
        switchDescr = 'Unassigned key'        
        createToolTip(self.action_blank3, switchDescr)
                    
        self.action_blank4 = ttk.Button(self.mvStatFunctKeys, text="  ", command=lambda: af.do_blank(self))
        self.action_blank4.grid(column=0, row=1, padx=4, pady=6)
        # Associated tool tip
        chgSgnDescr = 'Unassigned key'
        createToolTip(self.action_blank4, chgSgnDescr)
        
        self.action_blank5 = ttk.Button(self.mvStatFunctKeys, text="    ", command=lambda: af.do_blank(self))
        self.action_blank5.grid(column=1, row=1, padx=4, pady=6)
        # Associated tool tip
        invertXDescr = 'Unassigned key.'
        createToolTip(self.action_blank5, invertXDescr)
        
        self.action_blank6 = ttk.Button(self.mvStatFunctKeys, text="    ", command=lambda: af.do_blank(self))
        self.action_blank6.grid(column=2, row=1, padx=4, pady=6)
        # Associated tool tip
        squareXDescr = 'Unassigned key.'
        createToolTip(self.action_blank6, squareXDescr)
        
        self.action_blank7 = ttk.Button(self.mvStatFunctKeys, text="    ", command=lambda: af.do_blank(self))
        self.action_blank7.grid(column=3, row=1, padx=4, pady=6)
        # Associated tool tip
        xpowyDescr = 'Unassigned key.\n'
        createToolTip(self.action_blank7, xpowyDescr)

        self.action_blank8 = ttk.Button(self.mvStatFunctKeys, text="   ", command=lambda: af.do_blank(self))
        self.action_blank8.grid(column=4, row=1, padx=4, pady=6)
        # Associated tool tip
        sqrtDescr = 'Unassigned key\n'
        createToolTip(self.action_blank8, sqrtDescr)
        
        self.action_blank9 = ttk.Button(self.mvStatFunctKeys, text="  ", command=lambda: af.do_blank(self))
        self.action_blank9.grid(column=0, row=2, padx=4, pady=6)
        # Associated tool tip
        cosDescr = 'Unassigned key\n'
        createToolTip(self.action_blank9, cosDescr)
        
        self.action_blank10 = ttk.Button(self.mvStatFunctKeys, text="   ", command=lambda: af.do_blank(self))
        self.action_blank10.grid(column=1, row=2, padx=4, pady=6)
        # Associated tool tip
        sinDescr = 'Unassigned key.\n'
        createToolTip(self.action_blank10, sinDescr)
        
        self.action_blank11 = ttk.Button(self.mvStatFunctKeys, text="   ", command=lambda: af.do_blank(self))
        self.action_blank11.grid(column=2, row=2, padx=4, pady=6)
        # Associated tool tip
        tanDescr = 'Unassigned key.\n'
        createToolTip(self.action_blank11, tanDescr)
        
        self.action_blank12 = ttk.Button(self.mvStatFunctKeys, text="   ", command=lambda: af.do_blank(self))
        self.action_blank12.grid(column=3, row=2, padx=4, pady=6)
        # Associated tool tip
        arcCosineDescr = 'Unassigned key.\n'
        createToolTip(self.action_blank12, arcCosineDescr)
        
        self.action_blank13 = ttk.Button(self.mvStatFunctKeys, text="   ", command=lambda: af.do_blank(self))
        self.action_blank13.grid(column=4, row=2, padx=4, pady=6)
        # Associated tool tip
        arcsinDescr = 'Unassigned key\n'
        createToolTip(self.action_blank13, arcsinDescr)
        
        self.action_blank14 = ttk.Button(self.mvStatFunctKeys, text="   ", command=lambda: af.do_blank(self))
        self.action_blank14.grid(column=0, row=3, padx=4, pady=6)
        # Associated tool tip
        arctanDescr = 'Unassigned key\n'
        createToolTip(self.action_blank14, arctanDescr)
        
        self.action_blank15 = ttk.Button(self.mvStatFunctKeys, text="    ", command=lambda: af.do_blank(self))
        self.action_blank15.grid(column=1, row=3, padx=4, pady=6)
        # Associated tool tip
        log10Descr = 'Unassigned key.\n'
        createToolTip(self.action_blank15, log10Descr)
        
        self.action_blank16 = ttk.Button(self.mvStatFunctKeys, text="    ", command=lambda: af.do_blank(self))
        self.action_blank16.grid(column=2, row=3, padx=4, pady=6)
        # Associated tool tip
        lnDescr = 'Unassigned key\n'
        createToolTip(self.action_blank16, lnDescr)
        
        self.action_blank17 = ttk.Button(self.mvStatFunctKeys, text="   ", command=lambda: af.do_blank(self))
        self.action_blank17.grid(column=3, row=3, padx=4, pady=6)
        # Associated tool tip
        expDescr = 'Unassigned key\n'
        createToolTip(self.action_blank17, expDescr)
        
        self.action_blank18 = ttk.Button(self.mvStatFunctKeys, text="    ", command=lambda: af.do_blank(self))
        self.action_blank18.grid(column=4, row=3, padx=4, pady=6)
        # Associated tool tip
        factorialDescr = 'Unassigned key.\n'
        createToolTip(self.action_blank18, factorialDescr)
        
        self.action_blank19 = ttk.Button(self.mvStatFunctKeys, text="    ", command=lambda: af.do_blank(self))
        self.action_blank19.grid(column=0, row=4, padx=4, pady=6)
        # Associated tool tip
        xrootyDescr = 'Unassigned key.\n'
        createToolTip(self.action_blank19, xrootyDescr)
        
        self.action_blank20 = ttk.Button(self.mvStatFunctKeys, text="  ", command=lambda: af.do_blank(self))
        self.action_blank20.grid(column=1, row=4, padx=4, pady=6)
        # Associated tool tip
        blankDescr = 'Unassigned key'
        createToolTip(self.action_blank20, blankDescr)
        
        self.action_blank21 = ttk.Button(self.mvStatFunctKeys, text="   ", command=lambda: af.do_blank(self))
        self.action_blank21.grid(column=2, row=4, padx=4, pady=6)
        # Associated tool tip
        blankDescr = 'Unassigned key.\n'
        createToolTip(self.action_blank21, blankDescr)
        
        self.action_blank22 = ttk.Button(self.mvStatFunctKeys, text=" ", command=lambda: af.do_blank(self))
        self.action_blank22.grid(column=3, row=4, padx=4, pady=6)
        # Associated tool tip
        blankDescr = 'Unassigned key'
        createToolTip(self.action_blank22, blankDescr)
        
        # Convert degrees to radians
        self.action_blank23 = ttk.Button(self.mvStatFunctKeys, text="   ", command=lambda: af.do_blank(self))
        self.action_blank23.grid(column=4, row=4, padx=4, pady=6)
        # Associated tool tip
        deg2radDescr = 'Unassigned key\n'
        createToolTip(self.action_blank23, deg2radDescr)
        
        
        # ##########################################################
        # Creating a container frame to hold tab5 graphing widgets 
        # ##########################################################
        
        self.graphical = ttk.LabelFrame(tab5, text=' Graphical Output ', width=56)
        self.graphical.grid(column=0, row=0, padx=8, pady=4)
         
        # Adding a graphic window (canvas widget)
        gw = Canvas(self.graphical, width=460, height=550)
               
        gw.create_rectangle(20, 20, 400, 200, fill="blue") 
        gw.create_line(20, 190, 340, 20, fill="red", dash=(4, 4))
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
        fileMenu.add_command(label="Open")
        fileMenu.add_command(label="File Info", command=lambda: mg.getFileInfo(self))
        fileMenu.add_command(label="Reload Registers")
        fileMenu.add_command(label="Save Registers")
        
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self._quit)
        menuBar.add_cascade(label="File", menu=fileMenu)
        
        # Add an Edit Menu
        editMenu = Menu(menuBar, tearoff=0)
        editMenu.add_command(label="Cut")
        editMenu.add_command(label="Copy")
        editMenu.add_command(label="Paste")
        editMenu.add_command(label="Delete")
        editMenu.add_separator()
        editMenu.add_command(label="Clear All", command=lambda: af.do_clrAllRegr(self))
        editMenu.add_command(label="Select")
        editMenu.add_separator()
        editMenu.add_command(label="Options")
        menuBar.add_cascade(label="Edit", menu=editMenu)
        
        # Add an View Menu
        viewMenu = Menu(menuBar, tearoff=0)
        viewMenu.add_command(label="Toggle x/L Functions", command=lambda:af.do_toggleList(self))
        viewMenu.add_separator()
        viewMenu.add_command(label="Active Dataset", command=lambda: self.miscMessage("Dataset", "The currently active Dataset is \n{}".format(self.active_Dataset)))
        viewMenu.add_command(label="Table data", command=lambda:self.displaydfT())
        viewMenu.add_command(label="List data", command=self.displayL)
        viewMenu.add_command(label="Series data", command=self.displayS)
        viewMenu.add_command(label="Array data", command=self.displayArray)
        viewMenu.add_command(label="x and y", command=self.displayxy)
        menuBar.add_cascade(label="View", menu=viewMenu)
        
        # Add data menus
        dataMenu = Menu(menuBar, tearoff=0)
        dataMenu.add_command(label="New Table", command=lambda: af.loadData(self, "table dfT"))
        dataMenu.add_command(label="New Series 1", command=lambda:af.loadData(self, "series S1"))
        dataMenu.add_command(label="New Series 2", command=lambda:af.loadData(self, "series S2"))
        dataMenu.add_command(label="New List", command=lambda:af.loadData(self, "List L"))
        dataMenu.add_command(label="New Array", command=lambda:af.loadData(self, "array"))
        dataMenu.add_separator()
        dataMenu.add_command(label="Select Active Dataset", command=lambda: af.do_setActiveDataset(self))
        dataMenu.add_command(label="Load Active Data", command=lambda: af.loadData(self, active_Dataset))
        dataMenu.add_separator()
        dataMenu.add_command(label="Shift L to S1", command=lambda:af.convertData(self, "LtoS1)"))
        dataMenu.add_command(label="Shift S1 to S2", command=lambda:af.convertData(self, "S1toS2"))
        dataMenu.add_command(label="Shift S2 to L", command=lambda: af.convertData(self, "S2toL"))
        dataMenu.add_command(label="Make S1 and S2 to dataframe", command=lambda:af.convertData(self, "S1S2todf"))
        dataMenu.add_separator()
        dataMenu.add_command(label="Save Data")
        menuBar.add_cascade(label="Data", menu=dataMenu)
        
        # Add an tools Menu
        toolsMenu = Menu(menuBar, tearoff=0)
        toolsMenu.add_command(label="Munging")
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
        helpMenu.add_command(label="Calculator Documentation")
        helpMenu.add_command(label="Statistics Help")
        helpMenu.add_command(label="About", command=self.info)
        menuBar.add_cascade(label="Help", menu=helpMenu)

        # ~ end of menu bar ~ ------------------------------------------------- 

        
        # Set Focus to Tab
        tabControl.select(0)


        # Add a Tooltip to the Spinbox
# ~~ End of TKGUI CLass =======================================================        
        
        

#======================
# Start GUI
#======================

# ===============================================
# Unit Testing Code
# ===============================================
if __name__ == '__main__':
    print("tkGUI is running as main; \n    ie. a module self test")
    tkgui = calcGUI()
    tkgui.win.mainloop()
#~~~ END test code ==============================