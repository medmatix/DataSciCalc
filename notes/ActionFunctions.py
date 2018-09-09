'''
Created on Sep 8, 2018

@author: david
'''
import tkinter as tk
from DataSciCalc import calcGUI
from os import path, makedirs
import time
from datetime import datetime
import math as mt
import numpy as np


#=====================================================
# Class definitions
#=====================================================

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
    def do_clrx(self):
        # clear the entry in the current input register
        self.x = 0.0
        inxRegStr = ''
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, self.inxRegStr)
        print('cleared x register')
        
    def do_clrL(self):
        # clear the entry in the current input register
        self.L = 0.0
        self.y = 0.0
        inLRegStr = ''
        self.inLStr.delete(1.0,tk.END)
        self.inLStr.insert(tk.INSERT, self.inLRegStr)
        print('cleared List register')

    def do_clrAllRegr(self):
        # clear all the registers and variables for a  new calculation stream
        self.inxRegStr = ''
        self.inLRegStr = ''
        self.inxStr.delete(0, tk.END)
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.resVar = 0.0
        # log action to history 
        self.history.insert(tk.END, 'CLEAR ALL  ' + str(self.resVar) + '\n')
        self.history.see(tk.END)
        self.inxStr.insert(tk.INSERT, self.inxRegStr)
        print('cleared all registers and variables')
        print('current Register: ' + self.inxRegStr)
        print('current Variable: ' + str(self.x))
        print('Operand 2 Variable: ' + str(self.y))
    
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
        self.inxRegStr = self.inxRegStr +'0'        
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, self.inxRegStr)    
        self.xFlag = False
        print(self.inxRegStr)  
        print(0)            # check on value
        
    def append_digit1(self):        
        self.inxRegStr = self.inxRegStr + '1' 
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, self.inxRegStr)  
        self.xFlag = False  
        print(self.inxRegStr)              # check on value
        print(1)    
        
    def append_digit2(self):
        self.inxRegStr = self.inxRegStr + '2'        
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, self.inxRegStr)    
        self.xFlag = False
        print(self.inxRegStr) 
        print(2)
        
    def append_digit3(self):
        self.inxRegStr = self.inxRegStr + '3'        
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, self.inxRegStr)
        self.xFlag = False
        print(self.inxRegStr) 
        print(3)
        
    def append_digit4(self):
        self.inxRegStr = self.inxRegStr + '4'        
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, self.inxRegStr)
        self.xFlag = False
        print(self.inxRegStr) 
        print(4)    
        
    def append_digit5(self):
        self.inxRegStr = self.inxRegStr + '5'        
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, self.inxRegStr)
        self.xFlag = False
        print(self.inxRegStr) 
        print(5)
        
    def append_digit6(self):
        self.inxRegStr = self.inxRegStr + '6'        
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, self.inxRegStr)
        self.xFlag = False
        print(self.inxRegStr) 
        print(6)
        
    def append_digit7(self):
        self.inxRegStr = self.inxRegStr + '7'        
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, self.inxRegStr)
        self.xFlag = False
        print(self.inxRegStr) 
        print(7)    
        
    def append_digit8(self):
        self.inxRegStr = self.inxRegStr + '8'        
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, self.inxRegStr)    
        self.xFlag = False
        print(self.inxRegStr) 
        print(8)
        
    def append_digit9(self):
        self.inxRegStr = self.inxRegStr + '9'        
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, self.inxRegStr)
        self.xFlag = False
        print(self.inxRegStr) 
        print(9)
    def append_minsgn(self):
        self.inxRegStr = self.inxRegStr + '-'        
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, self.inxRegStr)    
        self.xFlag = False
        print(self.inxRegStr) 
        print('-')
        
    def append_dec(self):
        self.inxRegStr = self.inxRegStr + '.'        
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, self.inxRegStr)
        self.xFlag = False
        print(self.inxRegStr) 
        print('.')
        
    def append_comma(self):
        # append a comma to register
        self.inxRegStr = self.inxRegStr + ','        
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, self.inxRegStr)
        self.xFlag = False
        print(self.inxRegStr) 
        print(',')

    # doing operations and functions ------------------------------------------
    def do_add(self):
        # check for entered button
        if not self.xFlag:
            self.arithmeticError()
            return
        # add variables entered together
        self.resVar = self.y + self.x
        # log action to history 
        self.history.see(tk.END)
        # clear register before transfering result there
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, str(self.resVar))
        self.history.insert(tk.END, 'SUM  ' + str(self.resVar) + '\n')
        # set up for chain operation
        ActionFunctions.do_enterReg(self)
        print("adding")
        print("sum is {}".format(self.resVar))
        
    def do_subt(self):
        # check for entered button
        if not self.xFlag:
            self.arithmeticError()
            return
        # subtract variables entered 
        self.resVar = self.y - self.x
        # log action to history 
        self.history.see(tk.END)
        # clear register before transfering result there
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, str(self.resVar))
        self.history.insert(tk.END, 'DIFF  ' + str(self.resVar) + '\n')
        # set up for chain operation
        ActionFunctions.do_enterReg(self)

        print("subtracting")
        print("difference is {}".format(self.resVar))
        
    def do_mult(self):
        # check for entered button
        if not self.xFlag:
            self.arithmeticError()
            return
        # multiply variables entered 
        self.resVar = self.y * self.x
        # log action to history 
        
        self.history.see(tk.END)
        # clear register before transfering result there
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, str(self.resVar))
        self.history.insert(tk.END, 'PROD  ' + str(self.resVar) + '\n')
        # set up for chain operation
        ActionFunctions.do_enterReg(self)
        print("multiplying")
        print("product is {}".format(self.resVar))
        
    def do_div(self):
        # check for entered button
        if not self.xFlag:
            self.arithmeticError()
            return
        # divide variables entered, second from first         
        try:
            self.resVar = self.y / self.x
        except:
            self.improperInputError()
            return
        
        # log action to history 
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, str(self.resVar))
        self.history.insert(tk.END, 'DIVD  ' + str(self.resVar) + '\n')
        # set up for chain operation
        ActionFunctions.do_enterReg(self)

        print("dividing")
        print("dividend is {}".format(self.resVar))
        
    def do_enterx(self):
        self.y = self.x
        try:
            self.inxRegStr = self.inxStr.get()
            self.x = float(self.inxStr.get())
        except:
            self.castError()
            print("the x input can't be blank, a '0' is at least needed")
        ActionFunctions.do_clrx(self)
        # log action to history 
        #=======================================================================
        # self.history.insert(tk.END, 'x ENTERED  ' + str(self.x) + '\n')
        # self.history.see(tk.END)
        #=======================================================================
        self.xFlag = True
        self.inxStr.focus()
        print('current Register: ' + self.inxRegStr)
        print('current Variable: ' + str(self.x))
        print("Entered x register into x variable and clear x register")
        print('y Variable: ' + str(self.y))
        
    def do_enterL(self):
        self.y = self.x
        try:
            self.L=float(self.inLReg.get())
        except:
            self.castError()
            print("the input can't be blank, a '0' is atleast needed")
        ActionFunctions.do_clrL(self)
        # log action to history 
        self.history.insert(tk.END, 'ENTERED  ' + str(self.L) + '\n')
        self.history.see(tk.END)
        self.LFlag = True
        self.inxStr.focus()
        print('x Register: ' + self.inxRegStr)
        print('x Variable: ' + str(self.x))
        print("Entered x register into current variable and clear current register")
        print('Operand 2 Variable: ' + str(self.y))
        
    def do_xpowy(self):
        # check for entered button
        if not self.xFlag:
            self.arithmeticError()
            return
        self.resVar = (self.y)**(self.x)
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, str(self.resVar))
        self.history.insert(tk.END, 'x^y  ' + str(self.resVar) + '\n')
        self.history.see(tk.END)
        # set up for chain operation
        ActionFunctions.do_enterReg(self)

        # do something else to (x)
        print('x^y')
        print("y power of x is {}".format(self.resVar))
        
    def do_sqrt(self):
        # check for entered button
        if not self.xFlag:
            self.arithmeticError()
            return
        # calculate sqrt(x)
        self.resVar = mt.sqrt(self.x)
                # log action to history 
        
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, str(self.resVar))
        self.history.insert(tk.END, 'SQRT  ' + str(self.resVar) + '\n')
        self.history.see(tk.END)
        # set up for chain operation
        ActionFunctions.do_enterReg(self)

        print("square of x is {}".format(self.resVar))
        print('sqrt')
        
    def do_invert(self):
        # check for entered button
        if not self.xFlag:
            self.arithmeticError()
            return
        # calculate square of (x)
        self.resVar = 1/self.x
        # log action to history 
        
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, str(self.resVar))
        self.history.insert(tk.END, 'INVERSE  ' + str(self.resVar) + '\n')
        self.history.see(tk.END)
        # set up for chain operation
        ActionFunctions.do_enterReg(self)

        print("inverse of x is {}".format(self.resVar))
        print('inverse')
        print('inverse of x')
        # calculate inverse (x)
        print('inverted x')
    
    def do_power2(self):
        # check for entered button
        if not self.xFlag:
            self.arithmeticError()
            return
        # calculate square of (x)
        self.resVar = self.x**2
                # log action to history 
        
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, str(self.resVar))
        self.history.insert(tk.END, 'POWER2  ' + str(self.resVar) + '\n')
        self.history.see(tk.END)
        # set up for chain operation
        ActionFunctions.do_enterReg(self)

        print("square of x is {}".format(self.resVar))
        print('sqrt')
        print('squared x')
    
    def do_sgn(self):
        # check for entered button
        if not self.xFlag:
            ActionFunctions.do_enterReg(self)
        # do change of sign too (x)
        self.x = self.x * -1
        # log action to history 
        
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, str(self.x))
        self.history.insert(tk.END, ' +/- ' + str(self.x) + '\n')
        self.history.see(tk.END)
        print("sign changed, x is now {}".format(self.x))
        print('change of sign')
    
    def do_cos(self):
        # check for entered button
        if not self.xFlag:
            self.arithmeticError()
            return
        # calculate cos(x) (x in radians!!!
        self.resVar = mt.cos(self.x)
                # log action to history 
        
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, str(self.resVar))
        self.history.insert(tk.END, 'COS ' + str(self.resVar) + '\n')
        self.history.see(tk.END)
        # set up for chain operation
        ActionFunctions.do_enterReg(self)

        print("cosine of x is {}".format(self.resVar))
        print('cosine')
        
    def do_sin(self):
        # check for entered button
        if not self.xFlag:
            self.arithmeticError()
            return
        # calculate sqrt(x)
        self.resVar = mt.sin(self.x)
                # log action to history 
        
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, str(self.resVar))
        self.history.insert(tk.END, 'SIN ' + str(self.resVar) + '\n')
        self.history.see(tk.END)
        # set up for chain operation
        ActionFunctions.do_enterReg(self)

        print(" sine of x is {}".format(self.resVar))
        print('sine')
        
    def do_tan(self):
        # check for entered button
        if not self.xFlag:
            self.arithmeticError()
            return
        # calculate tangent(x)
        self.resVar = mt.tan(self.x)
                # log action to history 
        
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, str(self.resVar))
        self.history.insert(tk.END, 'TAN  ' + str(self.resVar) + '\n')
        self.history.see(tk.END)
        # set up for chain operation
        ActionFunctions.do_enterReg(self)

        print("tangent of x is {}".format(self.resVar))
        print('tangent')
        
    def do_acos(self):
        # check for entered button
        if not self.xFlag:
            self.arithmeticError()
            return
        # calculate cos(x) (x in radians!!!
        self.resVar = mt.acos(self.x)
                # log action to history 
        
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, str(self.resVar))
        self.history.insert(tk.END, 'COS ' + str(self.resVar) + '\n')
        self.history.see(tk.END)
        # set up for chain operation
        ActionFunctions.do_enterReg(self)

        print("cosine of x is {}".format(self.resVar))
        print('cosine')
        
    def do_asin(self):
        # check for entered button
        if not self.xFlag:
            self.arithmeticError()
            return
        # calculate sqrt(x)
        self.resVar = mt.asin(self.x)
                # log action to history 
        
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, str(self.resVar))
        self.history.insert(tk.END, 'SIN ' + str(self.resVar) + '\n')
        self.history.see(tk.END)
        # set up for chain operation
        ActionFunctions.do_enterReg(self)

        print(" sine of x is {}".format(self.resVar))
        print('sine')
        
    def do_atan(self):
        # check for entered button
        if not self.xFlag:
            self.arithmeticError()
            return
        # calculate tangent(x)
        self.resVar = mt.atan(self.x)
                # log action to history 
        
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, str(self.resVar))
        self.history.insert(tk.END, 'TAN  ' + str(self.resVar) + '\n')
        self.history.see(tk.END)
        # set up for chain operation
        ActionFunctions.do_enterReg(self)

        print("tangent of x is {}".format(self.resVar))
        print('tangent')
    def do_log10(self):
        # check for entered button
        if not self.xFlag:
            self.arithmeticError()
            return
        # calculate base 10 log(x)
        try:
            self.resVar = mt.log10(self.x)
        except:
            self.improperInputError()
            return
        # log action to history 
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, str(self.resVar))
        self.history.insert(tk.END, 'LOG10  ' + str(self.resVar) + '\n')
        self.history.see(tk.END)
        # set up for chain operation
        ActionFunctions.do_enterReg(self)

        print("log10 of x is {}".format(self.resVar))
        print('LOG')
        
    def do_ln(self):
        # check for entered button
        if not self.xFlag:
            self.arithmeticError()
            return
        # calculate natural log(x)
        try:
            self.resVar = mt.log(self.x)
        except:
            self.improperInputError()
            return
        
        # log action to history 
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, str(self.resVar))
        self.history.insert(tk.END, 'LN  ' + str(self.resVar) + '\n')
        self.history.see(tk.END)
        # set up for chain operation
        ActionFunctions.do_enterReg(self)

        print("ln of x is {}".format(self.resVar))
        print('ln')
        
    def get_pi(self):
        # get constant pi
        self.x = mt.pi
        # log action to history 
        
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, str(self.x))
        self.history.insert(tk.END, ' PI ' + str(self.x) + '\n')
        self.history.see(tk.END)
        self.xFlag = True
        self.inxStr.focus()
        print("PI is {}".format(self.x))
        print('pi ')
        
    def do_exp(self):
        # check for entered button
        if not self.xFlag:
            self.arithmeticError()
            return
        # calculate exp(x)
        self.resVar = mt.exp(self.x)
                # log action to history 
        
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, str(self.resVar))
        self.history.insert(tk.END, 'EXP  ' + str(self.resVar) + '\n')
        self.history.see(tk.END)
        # set up for chain operation
        ActionFunctions.do_enterReg(self)

        print("exp of x is {}".format(self.resVar))
        print('exp()')
        
    def get_e(self):
        # get constant e
        self.x = mt.e
        # log action to history 
        
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, str(self.x))
        self.history.insert(tk.END, ' e is ' + str(self.x) + '\n')
        self.history.see(tk.END)
        self.xFlag = True
        self.inxStr.focus()
        print("e is {}".format(self.x))
        print(' e ')
        
    def get_phi(self):
        # calculate PHI - golden ratio
        self.x = (1 + mt.sqrt(5))/2
        # log action to history 
        
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, str(self.x))
        self.history.insert(tk.END, ' PHI is ' + str(self.x) + '\n')
        self.history.see(tk.END)
        self.xFlag = True
        self.inxStr.focus()
        print("golden ratio (PHI) is {}".format(self.x))
        print(" phi ")
        
    def do_deg2rad(self):
        # check for entered button
        if not self.xFlag:
            self.arithmeticError()
            return
        # convert degrees in x to radians (x)
        self.resVar = mt.radians(self.x)
                # log action to history 
        
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, str(self.resVar))
        self.history.insert(tk.END, 'DEG2RAD  ' + str(self.resVar) + '\n')
        self.history.see(tk.END)
        # set up for chain operation
        ActionFunctions.do_enterReg(self)

        print("Deg to Radians of x is {}".format(self.resVar))
        print('DEG2RAD')
    
    def do_blank(self):
        # check for entered button
        if not self.xFlag:
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
        
    def do_clr_history(self, scr_notes):
        # clear the calculation history
        scr_notes.delete(1.0,tk.END)
        #self.history.insert(tk.END, 'CLEAR HISTORY\n')
        scr_notes.see(tk.END)
        print('cleared the notes pad')
        
    def do_prt_history(self, scr_notes):
        print("\n Notes:\n")
        print(scr_notes.get(1.0, tk.END) + '\n')  # to Console
        self.history.insert(tk.END, 'PRINT NOTES \n')
        self.history.see(tk.END)
        self.notesToDialog()  # and show in a dialog
        
    def do_log_history(self):
        self.history.insert(tk.END, self.scr_notes.get(1.0, tk.END) + '\n')
        self.history.see(tk.END)
        
    def do_save_history(self):
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