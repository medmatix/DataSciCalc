'''
Module: Function Key action methods for DataSciCalc Calculator
Created on Sep 8, 2018
updated Sep 21, 2018 13:46PM

@version: DSC0.019
@license: MIT
@author: David York
@copyright: 2018 David A York
'''
import tkinter as tk
from os import path, makedirs
import time
from datetime import datetime
import math as mt
import statistics as st
import numpy as np
from scipy import stats
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from builtins import list


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

    # Register and variable cleanup functions ############################
    '''
    Key pad Implementation Functions and Methods
    '''
        
    def do_clrx(self):
        # clear the entry in the current input register
        self.inxRegStr = ''
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, self.inxRegStr)
        self.history.insert(tk.END, 'CLEAR x Reg \n')
        self.history.see(tk.END)
        print('cleared x register')
        
    def do_clrL(self):
        # clear the entry in the current input register
        self.inLRegStr = ''
        self.inLStr.delete(1.0,tk.END)
        self.inLStr.insert(tk.INSERT, self.inLRegStr)
        self.history.insert(tk.END, 'CLEAR L Reg \n')
        self.history.see(tk.END)
        print('cleared List register')

    def do_clrAllRegr(self):
        # clear all the registers and variables for a  new calculation stream
        self.inxRegStr = ''
        self.inLRegStr = ''
        self.inxStr.delete(0, tk.END)
        self.inLStr.delete(1.0, tk.END)
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.L = [0]
        self.resVar = 0.0
        self.Lflag = False
        self.xFlag = False
        # log action to history 
        self.history.insert(tk.END, 'CLEAR ALL \n')
        self.history.see(tk.END)
        self.inxStr.insert(tk.INSERT, self.inxRegStr)
        self.inLStr.insert(tk.INSERT, self.inLRegStr)
        print('cleared all registers and variables')

    
    def do_enterx(self):
        self.y = self.x
        self.yValStr['text'] = str(self.y)
        try:
            self.inxRegStr = self.inxStr.get()
            self.x = float(self.inxStr.get())
        except:
            self.castError()
            print("the x input can't be blank, a '0' is at least needed")
        ActionFunctions.do_clrx(self)
        # log action to history 
        self.history.insert(tk.END, 'x ENTERED  ' + str(self.x) + '\n')
        self.history.see(tk.END)
        self.xFlag = True
        self.inxStr.focus()
        print('current Register: ' + self.inxRegStr)
        print('current Variable: ' + str(self.x))
        print("Entered x register into x variable and clear x register")
        print('y Variable: ' + str(self.y))
        
    def do_enterL(self):
        tmpL = []
        try:
            self.inLRegStr = self.inLStr.get(1.0, tk.END).split(',')
            print(self.inLRegStr)
            for i in self.inLRegStr:
                tmpL.append(float(i))
            self.L = tmpL
            tmpL = [] 
        except:
            self.listError()
            print("There is an error in the list entry")
        # log action to history        
        self.history.insert(tk.END, 'LIST ENTERED  ' + str(self.L) + '\n')
        self.history.see(tk.END)
        self.Lflag = True
        self.xyFunctKeys.grid_forget()
        self.listFunctKeys.grid()
        self.inLStr.focus()
        print('list L is: ' + str(self.L))

        
    def do_appendx(self):
        tmpL = self.L
        self.y = self.x
        self.yValStr['text'] = str(self.y)
        try:
            self.inxRegStr = self.inxStr.get()
            tmpxs = self.inxRegStr
            print(tmpxs)
            tmpxf = float(tmpxs)
            print("x to l = {}".format(tmpxf))
            tmpL.append(tmpxf)
            print(tmpL)
            print(self.L)
        except:
            self.castError()
            print("the x input can't be blank, a '0' is at least needed")
            return
        self.inLStr.delete(1.0,tk.END)
        self.inLStr.insert(tk.INSERT, self.L.__str__())
        ActionFunctions.do_clrx(self)
        # log action to history 
        self.history.insert(tk.END, 'x ENTERED  ' + str(self.x) + '\n')
        self.history.see(tk.END)
        self.xFlag = True
        self.inxStr.focus()
        print('current Register: ' + self.inxRegStr)
        print('current Variable: ' + str(self.x))
        print("Entered x register into x variable and clear x register")
        print('y Variable: ' + str(self.y))
    
    # appending digits to input    
    
    def append_digit0(self):
        self.inxRegStr = self.inxRegStr + '0' 
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, self.inxRegStr)  
        self.xFlag = False  
        
    def append_digit1(self):        
        self.inxRegStr = self.inxRegStr + '1' 
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, self.inxRegStr)  
        self.xFlag = False  
        
    def append_digit2(self):
        self.inxRegStr = self.inxRegStr + '2'        
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, self.inxRegStr)    
        self.xFlag = False
        
    def append_digit3(self):
        self.inxRegStr = self.inxRegStr + '3'        
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, self.inxRegStr)
        self.xFlag = False
        
    def append_digit4(self):
        self.inxRegStr = self.inxRegStr + '4'        
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, self.inxRegStr)
        self.xFlag = False
        
    def append_digit5(self):
        self.inxRegStr = self.inxRegStr + '5'        
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, self.inxRegStr)
        self.xFlag = False
        
    def append_digit6(self):
        self.inxRegStr = self.inxRegStr + '6'        
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, self.inxRegStr)
        self.xFlag = False
        
    def append_digit7(self):
        self.inxRegStr = self.inxRegStr + '7'        
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, self.inxRegStr)
        self.xFlag = False
        
    def append_digit8(self):
        self.inxRegStr = self.inxRegStr + '8'        
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, self.inxRegStr)    
        self.xFlag = False
        
    def append_digit9(self):
        self.inxRegStr = self.inxRegStr + '9'        
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, self.inxRegStr)
        self.xFlag = False

    def append_minsgn(self):
        self.inxRegStr = self.inxRegStr + '-'        
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, self.inxRegStr)    
        self.xFlag = False
        
    def append_dec(self):
        self.inxRegStr = self.inxRegStr + '.'        
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, self.inxRegStr)
        self.xFlag = False
        
    def append_comma(self):
        # append a comma to register
        self.inxRegStr = self.inxRegStr + ','        
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, self.inxRegStr)
        self.xFlag = False


    # doing discrete XY operations and functions #######################
    '''
    Discrete Variable Functions
    '''
        
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
        self.x = self.resVar
        self.xFlag = True
        self.inxStr.focus()
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
        self.x = self.resVar
        self.xFlag = True
        self.inxStr.focus()

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
        self.x = self.resVar
        self.xFlag = True
        self.inxStr.focus()
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
        self.x = self.resVar
        self.xFlag = True
        self.inxStr.focus()

        print("dividing")
        print("dividend is {}".format(self.resVar))
    
    def do_switchxy(self):
        temp = self.y
        self.y = self.x
        self.x = temp
        self.yValStr['text'] = str(self.y)
        self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, str(self.x))
        self.history.insert(tk.END, 'EXCHG X & Y  \n' + 'x = ' + str(self.x)+',  y = ' + str(self.y) + '\n')
        
        print ('switch x and y')
        print ('x = {}, y = {}'.format(self.x, self.y))
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
        self.x = self.resVar
        self.xFlag = True
        self.inxStr.focus()

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
        self.x = self.resVar
        self.xFlag = True
        self.inxStr.focus()

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
        self.x = self.resVar
        self.xFlag = True
        self.inxStr.focus()

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
        self.x = self.resVar
        self.xFlag = True
        self.inxStr.focus()

        print("square of x is {}".format(self.resVar))
        print('sqrt')
        print('squared x')
    
    def do_sgn(self):
        # check for entered button
        if not self.xFlag:
            ActionFunctions.do_enterx(self)
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
        self.x = self.resVar
        self.xFlag = True
        self.inxStr.focus()

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
        self.x = self.resVar
        self.xFlag = True
        self.inxStr.focus()

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
        self.x = self.resVar
        self.xFlag = True
        self.inxStr.focus()

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
        self.x = self.resVar
        self.xFlag = True
        self.inxStr.focus()

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
        self.x = self.resVar
        self.xFlag = True
        self.inxStr.focus()

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
        self.x = self.resVar
        self.xFlag = True
        self.inxStr.focus()

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
        self.x = self.resVar
        self.xFlag = True
        self.inxStr.focus()

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
        self.x = self.resVar
        self.xFlag = True
        self.inxStr.focus()

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
        self.x = self.resVar
        self.xFlag = True
        self.inxStr.focus()

        print("exp of x is {}".format(self.resVar))
        print('exp()')
        
    def do_factorial(self):
        print("factorial pending")
        
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
        self.x = self.resVar
        self.xFlag = True
        self.inxStr.focus()

        print("Deg to Radians of x is {}".format(self.resVar))
        print('DEG2RAD')
    
    # doing L x  operations and functions ------------------------------------------
    def do_addL(self):
        # check for entered button
        if not self.xFlag:
            self.arithmeticError()
            return
        if not self.Lflag:
            self.arithmeticError()
            return
        # add variables entered together
        newL =  [i + self.x for i in self.L]
        self.L = newL
        # log action to history 
        self.history.see(tk.END)
        # clear register before transfering result there
        if (len(self.inLStr.get(1.0,tk.END))) > 0:
            self.inLStr.delete(1.0,tk.END)
            print("cleared")
        self.inLStr.insert(tk.INSERT, str(self.L))            
        self.history.insert(tk.END, 'x ADDto L  ' + str(self.L) + '\n')
        # set up for chain operation
        self.x = 0
        self.xFlag = True
        self.inxStr.focus()
        print("adding x to L")
        print("L + x is {}".format(self.L))
        
    def do_subtL(self):
        # check for entered button
        if not self.xFlag:
            self.arithmeticError()
            return
        if not self.Lflag:
            self.arithmeticError()
            return
        # add variables entered together
        newL =  [i - self.x for i in self.L]
        self.L = newL
        # log action to history 
        self.history.see(tk.END)
        # clear register before transferring result there
        if (len(self.inLStr.get(1.0,tk.END))) > 0:
            self.inLStr.delete(1.0,tk.END)
            print("cleared")
        self.inLStr.insert(tk.INSERT, str(self.L))
        self.history.insert(tk.END, 'x SUBTfrom L  ' + str(self.L) + '\n')
        # set up for chain operation
        self.x = 0
        self.xFlag = True
        self.inxStr.focus()

        print("subtracting x from all L")
        print("differences are {}".format(self.L))
        
    def do_multL(self):
        # check for entered button
        if not self.xFlag:
            self.arithmeticError()
            return
        if not self.Lflag:
            self.arithmeticError()
            return
        # add variables entered together
        newL =  [i * self.x for i in self.L]
        self.L = newL
        # log action to history 
        self.history.see(tk.END)
        # clear register before transferring result there
        if (len(self.inLStr.get(1.0,tk.END))) > 0:
            self.inLStr.delete(1.0,tk.END)
            print("cleared")
        self.inLStr.insert(tk.INSERT, str(self.L))
        self.history.insert(tk.END, 'L MULTby x  ' + str(self.L) + '\n')
        # set up for chain operation
        self.x = 0
        self.xFlag = True
        self.inxStr.focus()
        print("multiplying L by")
        print("product is {}".format(self.L))
        
    def do_divL(self):
        # check for entered button
        if not self.xFlag:
            self.arithmeticError()
            return
        if not self.Lflag:
            self.arithmeticError()
            return
        # add variables entered together
        newL =  [i / self.x for i in self.L]
        self.L = newL
        # log action to history 
        self.history.see(tk.END)
        # clear register before transferring result there
        if (len(self.inLStr.get(1.0,tk.END))) > 0:
            self.inLStr.delete(1.0,tk.END)
            print("cleared")
        self.inLStr.insert(tk.INSERT, str(self.L))
        self.history.insert(tk.END, 'L DIVby x  ' + str(self.L) + '\n')
        # set up for chain operation
        self.x = 0
        self.xFlag = True
        self.inxStr.focus()

        print("dividing L by x")
        print("dividend is {}".format(self.L))
        
    # List Functions #######################################
    
    '''
    List Mathematics FUnctions
    '''
        
    def do_sumL(self):
        # check for entered button
        if not self.Lflag:
            self.arithmeticError()
            return
        # add variables entered together
        self.x =  sum(self.L)
        # log action to history 
        self.history.see(tk.END)
        # clear register before transferring result there
        if (len(self.inLStr.get(1.0,tk.END))) > 0:
            self.inLStr.delete(1.0,tk.END)
        if (len(self.inxStr.get())) > 0:
            self.inxStr.delete(0,tk.END)
            print("cleared")
        self.inxStr.insert(tk.INSERT, str(self.x))
        self.inLStr.insert(tk.INSERT, str(self.L))
        self.history.insert(tk.END, 'SUM of L  ' + str(self.x) + '\n')
        # set up for chain operation
        self.xFlag = True
        self.inxStr.focus()
        print("sum L")
        print("sum is {}".format(self.x))

      
    def do_prodL(self):
        # check for entered button
        if not self.Lflag:
            self.arithmeticError()
            return
        # add variables entered together
        self.x =  np.prod(self.L)
        # log action to history 
        self.history.see(tk.END)
        # clear register before transferring result there

        if (len(self.inxStr.get())) > 0:
            self.inxStr.delete(0,tk.END)

        self.inxStr.insert(tk.INSERT, str(self.x))
        self.inLStr.insert(tk.INSERT, str(self.L))
        self.history.insert(tk.END, 'PROD of L  ' + str(self.x) + '\n')
        # set up for chain operation
        self.xFlag = True
        self.inxStr.focus()
        print("PROD L")
        print("product is {}".format(self.x))
        
    def do_sqrtL(self):
        # check for entered button
        if not self.Lflag:
            self.arithmeticError()
            return
        # add variables entered together
        newL =  [mt.sqrt(i) for i in self.L]
        self.L = newL
        # log action to history 
        self.history.see(tk.END)
        # clear register before transferring result there
        if (len(self.inLStr.get(1.0,tk.END))) > 0:
            self.inLStr.delete(1.0,tk.END)
            print("cleared")
        self.inLStr.insert(tk.INSERT, str(self.L))
        self.history.insert(tk.END, 'L squared' + str(self.L) + '\n')
        # set up for chain operation
        self.x = 0
        self.xFlag = True
        self.inxStr.focus()
        print("L squared")
        print("L squared is {}".format(self.L))

        
    def do_invertL(self):
        # check for entered button
        if not self.Lflag:
            self.arithmeticError()
            return
        # add variables entered together
        newL =  [1/i for i in self.L]
        self.L = newL

        # log action to history 
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inLStr.delete(1.0,tk.END)
        self.inLStr.insert(tk.INSERT, str(self.L))
        self.history.insert(tk.END, 'INVERSE of L' + str(self.L) + '\n')
        self.history.see(tk.END)
        # set up for chain operation
        self.xFlag = True
        self.inxStr.focus()

        print("inverse of x is {}".format(self.resVar))
        print('inverse')
        print('inverse of x')
        # calculate inverse (x)
        print('inverted x')
        
            # do something else to (x)
        print('x^y')
        print("y power of x is {}".format(self.resVar))
        
    def do_Lpowx(self):
        # check for entered button
        if not self.xFlag:
            self.arithmeticError()
            return
        if not self.Lflag:
            self.arithmeticError()
            return
        # add variables entered together
        newL =  [i**self.x for i in self.L]
        self.L = newL
        # log action to history 
        self.history.see(tk.END)
        # clear register before transferring result there
        if (len(self.inLStr.get(1.0,tk.END))) > 0:
            self.inLStr.delete(1.0,tk.END)
            print("cleared")
        self.inLStr.insert(tk.INSERT, str(self.L))
        self.history.insert(tk.END, 'L toPOWER x  ' + str(self.L) + '\n')
        # set up for chain operation
        self.x = 0
        self.xFlag = True
        self.inxStr.focus()
        print("L toPOWER x")
        print("result list is {}".format(self.L))
        
        
    def do_Lpower2(self):
        # check for entered button
        if not self.Lflag:
            self.arithmeticError()
            return
        # add variables entered together
        newL =  [i**2 for i in self.L]
        self.L = newL
        # log action to history 
        self.history.see(tk.END)
        # clear register before transferring result there
        if (len(self.inLStr.get(1.0,tk.END))) > 0:
            self.inLStr.delete(1.0,tk.END)
            print("cleared")
        self.inLStr.insert(tk.INSERT, str(self.L))
        self.history.insert(tk.END, 'L squared' + str(self.L) + '\n')
        # set up for chain operation
        self.x = 0
        self.xFlag = True
        self.inxStr.focus()
        print("L squared")
        print("L squared is {}".format(self.L))

    
    def do_sgnL(self):
        # check for entered button
        if not self.Lflag:
            self.arithmeticError()
            return
        # do change of sign too (x)
        self.L = [i*(-1) for i in self.L]
        # log action to history 
        
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inLStr.delete(1.0,tk.END)
        self.inLStr.insert(tk.INSERT, str(self.L))
        self.history.insert(tk.END, ' +/- ' + str(self.L) + '\n')
        self.history.see(tk.END)
        print("sign changed, L is now {}".format(self.L))
        print('change of sign all L')
    
    def do_cosL(self):
        # check for entered button
        if not self.Lflag:
            self.arithmeticError()
            return
        # add variables entered together
        newL =  [mt.cos(i) for i in self.L]
        self.L = newL

        # log action to history 
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inLStr.delete(1.0,tk.END)
        self.inLStr.insert(tk.INSERT, str(self.L))
        self.history.insert(tk.END, 'cosine of L' + str(self.L) + '\n')
        self.history.see(tk.END)
        # set up for chain operation
        self.xFlag = True
        self.inxStr.focus()

        print("cosine of L is {}".format(self.L))
        print('cosine')
        
    def do_sinL(self):
        # check for entered button
        if not self.Lflag:
            self.arithmeticError()
            return
        # add variables entered together
        newL =  [mt.sin(i) for i in self.L]
        self.L = newL

        # log action to history 
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inLStr.delete(1.0,tk.END)
        self.inLStr.insert(tk.INSERT, str(self.L))
        self.history.insert(tk.END, 'sine of L' + str(self.L) + '\n')
        self.history.see(tk.END)
        # set up for chain operation
        self.xFlag = True
        self.inxStr.focus()

        print("sine of L is {}".format(self.L))
        print('sine')
        
    def do_tanL(self):
        # check for entered button
        if not self.Lflag:
            self.arithmeticError()
            return
        # add variables entered together
        newL =  [mt.tan(i) for i in self.L]
        self.L = newL

        # log action to history 
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inLStr.delete(1.0,tk.END)
        self.inLStr.insert(tk.INSERT, str(self.L))
        self.history.insert(tk.END, 'tangent of L' + str(self.L) + '\n')
        self.history.see(tk.END)
        # set up for chain operation
        self.xFlag = True
        self.inxStr.focus()

        print("tangent of L is {}".format(self.L))
        print('tangent')
        
    def do_acosL(self):
        # check for entered button
        if not self.Lflag:
            self.arithmeticError()
            return
        # add variables entered together
        newL =  [mt.acos(i) for i in self.L]
        self.L = newL

        # log action to history 
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inLStr.delete(1.0,tk.END)
        self.inLStr.insert(tk.INSERT, str(self.L))
        self.history.insert(tk.END, 'arcCosine of L' + str(self.L) + '\n')
        self.history.see(tk.END)
        # set up for chain operation
        self.xFlag = True
        self.inxStr.focus()

        print("arcCosine of L is {}".format(self.L))
        print('arcCosine')
        
    def do_asinL(self):
        # check for entered button
        if not self.Lflag:
            self.arithmeticError()
            return
        # add variables entered together
        newL =  [mt.asin(i) for i in self.L]
        self.L = newL

        # log action to history 
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inLStr.delete(1.0,tk.END)
        self.inLStr.insert(tk.INSERT, str(self.L))
        self.history.insert(tk.END, 'arcsine of L' + str(self.L) + '\n')
        self.history.see(tk.END)
        # set up for chain operation
        self.xFlag = True
        self.inxStr.focus()

        print("arcsine of L is {}".format(self.L))
        print('arcsine')
        
    def do_atanL(self):
        # check for entered button
        if not self.Lflag:
            self.arithmeticError()
            return
        # add variables entered together
        newL =  [mt.atan(i) for i in self.L]
        self.L = newL

        # log action to history 
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inLStr.delete(1.0,tk.END)
        self.inLStr.insert(tk.INSERT, str(self.L))
        self.history.insert(tk.END, 'arctan of L' + str(self.L) + '\n')
        self.history.see(tk.END)
        # set up for chain operation
        self.xFlag = True
        self.inxStr.focus()

        print("arctan of L is {}".format(self.L))
        print('arctan')
        
    def do_log10L(self):
        # check for entered button
        if not self.Lflag:
            self.arithmeticError()
            return
        # add variables entered together
        newL =  [mt.log10(i) for i in self.L]
        self.L = newL

        # log action to history 
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inLStr.delete(1.0,tk.END)
        self.inLStr.insert(tk.INSERT, str(self.L))
        self.history.insert(tk.END, 'log10 of L' + str(self.L) + '\n')
        self.history.see(tk.END)
        # set up for chain operation
        self.xFlag = True
        self.inxStr.focus()

        print("log10 of L is {}".format(self.L))
        print('Log10')

        
    def do_10powL(self):
        # check for entered button
        if not self.Lflag:
            self.arithmeticError()
            return
        # add variables entered together
        newL =  [10**i for i in self.L]
        self.L = newL
        # log action to history 
        self.history.see(tk.END)
        # clear register before transferring result there
        if (len(self.inLStr.get(1.0,tk.END))) > 0:
            self.inLStr.delete(1.0,tk.END)
            print("cleared")
        self.inLStr.insert(tk.INSERT, str(self.L))
        self.history.insert(tk.END, '10 toPOWER of all L  ' + str(self.L) + '\n')
        # set up for chain operation
        self.x = 0
        self.xFlag = True
        self.inxStr.focus()
        print("10 toPOWER L")
        print("10 to power of L is {}".format(self.L))

        
    def do_lnL(self):
        # check for entered button
        if not self.Lflag:
            self.arithmeticError()
            return
        # add variables entered together
        newL =  [mt.log(i) for i in self.L]
        self.L = newL
        # log action to history 
        self.history.see(tk.END)
        # clear register before transferring result there
        if (len(self.inLStr.get(1.0,tk.END))) > 0:
            self.inLStr.delete(1.0,tk.END)
            print("cleared")
        self.inLStr.insert(tk.INSERT, str(self.L))
        self.history.insert(tk.END, 'ln of all L  ' + str(self.L) + '\n')
        # set up for chain operation
        self.x = 0
        self.xFlag = True
        self.inxStr.focus()
        print("ln L")
        print("ln L is {}".format(self.L))

        
    def do_expL(self):
        # check for entered button
        if not self.Lflag:
            self.arithmeticError()
            return
        # add variables entered together
        newL =  [mt.exp(i) for i in self.L]
        self.L = newL
        # log action to history 
        self.history.see(tk.END)
        # clear register before transferring result there
        if (len(self.inLStr.get(1.0,tk.END))) > 0:
            self.inLStr.delete(1.0,tk.END)
            print("cleared")
        self.inLStr.insert(tk.INSERT, str(self.L))
        self.history.insert(tk.END, 'EXP L  ' + str(self.L) + '\n')
        # set up for chain operation
        self.x = 0
        self.xFlag = True
        self.inxStr.focus()
        print("EXP L")
        print("exp of L is {}".format(self.L))
        
    def do_xrootL(self):
        # check for entered button
        if not self.xFlag:
            self.arithmeticError()
            return
        # check for entered button
        if not self.xFlag:
            self.arithmeticError()
            return
        if not self.Lflag:
            self.arithmeticError()
            return
        # add variables entered together
        newL =  [(mt.exp(i)/self.x) for i in self.L]
        self.L = newL
        # log action to history 
        self.history.see(tk.END)
        # clear register before transferring result there
        if (len(self.inLStr.get(1.0,tk.END))) > 0:
            self.inLStr.delete(1.0,tk.END)
        self.inLStr.insert(tk.INSERT, str(self.L))
        self.history.insert(tk.END, 'xROOTL  ' + str(self.L) + '\n')
        # set up for chain operation
        self.x = 0
        self.xFlag = True
        self.inxStr.focus()
        print("x root L")
        print("x root of L is {}".format(self.L))
        
    def do_Ldeg2Lrad(self):
        # check for entered button
        if not self.Lflag:
            self.arithmeticError()
            return
        # add variables entered together
        newL =  [mt.radians(i) for i in self.L]
        self.L = newL
        # log action to history 
        self.history.see(tk.END)
        # clear register before transferring result there
        if (len(self.inLStr.get(1.0,tk.END))) > 0:
            self.inLStr.delete(1.0,tk.END)
        self.inLStr.insert(tk.INSERT, str(self.L))
        self.history.insert(tk.END, 'DEG2RAD L  ' + str(self.L) + '\n')
        # set up for chain operation
        self.x = 0
        self.xFlag = True
        self.inxStr.focus()
        print('DEG2RAD')
        print("Deg to Radians of L is {}".format(self.L))
        
    '''
    List Statistics Functions 
    '''
        
    def do_LStats(self):
            self.listFunctKeys.grid_forget()
            self.xyFunctKeys.grid_forget()
            self.listStatsKeys.grid() 
            
    def do_meanL(self):
        if not self.Lflag:
            self.arithmeticError()
            return
        # add variables entered together
        self.x =  st.mean(self.L)
        # log action to history 
        self.history.see(tk.END)
        # clear register before transferring result there
        if (len(self.inLStr.get(1.0,tk.END))) > 0:
            self.inLStr.delete(1.0,tk.END)
        if (len(self.inxStr.get())) > 0:
            self.inxStr.delete(0,tk.END)
            print("cleared")
        self.inxStr.insert(tk.INSERT, str(self.x))
        self.inLStr.insert(tk.INSERT, str(self.L))
        self.history.insert(tk.END, 'MEAN of L  ' + str(self.x) + '\n')
        # set up for chain operation
        self.xFlag = True
        self.inxStr.focus()
        print("mean L")
        print("mean of L is {}".format(self.x)) 

    def do_medianL(self):
        if not self.Lflag:
            self.arithmeticError()
            return
        # add variables entered together
        self.x =  st.median(self.L)
        # log action to history 
        self.history.see(tk.END)
        # clear register before transferring result there
        if (len(self.inxStr.get())) > 0:
            self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, str(self.x))
        self.inLStr.insert(tk.INSERT, str(self.L))
        self.history.insert(tk.END, 'MEDIAN of L  ' + str(self.x) + '\n')
        # set up for chain operation
        self.xFlag = True
        self.inxStr.focus()
        print("median L")
        print("median of L is {}".format(self.x)) 
        
    def do_minL(self):
        if not self.Lflag:
            self.arithmeticError()
            return
        # add variables entered together
        self.x =  min(self.L)
        # log action to history 
        self.history.see(tk.END)
        # clear register before transferring result there
        if (len(self.inxStr.get())) > 0:
            self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, str(self.x))
        self.inLStr.insert(tk.INSERT, str(self.L))
        self.history.insert(tk.END, 'MIN of L  ' + str(self.x) + '\n')
        # set up for chain operation
        self.xFlag = True
        self.inxStr.focus()
        print("minimum L")
        print("minimum value of L is {}".format(self.x))
        
    def do_maxL(self):
        if not self.Lflag:
            self.arithmeticError()
            return
        # add variables entered together
        self.x =  max(self.L)
        # log action to history 
        self.history.see(tk.END)
        # clear register before transferring result there
        if (len(self.inxStr.get())) > 0:
            self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, str(self.x))
        self.inLStr.insert(tk.INSERT, str(self.L))
        self.history.insert(tk.END, 'MAX of L  ' + str(self.x) + '\n')
        # set up for chain operation
        self.xFlag = True
        self.inxStr.focus()
        print("maximum L")
        print("maximum value of L is {}".format(self.x))
        
    def do_pstdevL(self):
        if not self.Lflag:
            self.arithmeticError()
            return
        # add variables entered together
        self.x =  st.pstdev(self.L)
        # log action to history 
        self.history.see(tk.END)
        # clear register before transferring result there
        if (len(self.inxStr.get())) > 0:
            self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, str(self.x))
        self.inLStr.insert(tk.INSERT, str(self.L))
        self.history.insert(tk.END, 'PSD of L  ' + str(self.x) + '\n')
        # set up for chain operation
        self.xFlag = True
        self.inxStr.focus()
        print("pop StDev L")
        print("Pop StDev of L is {}".format(self.x))
        
    def do_countL(self):
        if not self.Lflag:
            self.arithmeticError()
            return
        # add variables entered together
        self.x =  len(self.L)
        # log action to history 
        self.history.see(tk.END)
        # clear register before transferring result there
        if (len(self.inxStr.get())) > 0:
            self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, str(self.x))
        self.inLStr.insert(tk.INSERT, str(self.L))
        self.history.insert(tk.END, 'n of L  ' + str(self.x) + '\n')
        # set up for chain operation
        self.xFlag = True
        self.inxStr.focus()
        print("n L")
        print("n of L is {}".format(self.x))
        
    def do_quartile1L(self):
        if not self.Lflag:
            self.arithmeticError()
            return
        # add variables entered together
        self.x =  np.percentile(self.L, 25)
        # log action to history 
        self.history.see(tk.END)
        # clear register before transferring result there
        if (len(self.inxStr.get())) > 0:
            self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, str(self.x))
        self.inLStr.insert(tk.INSERT, str(self.L))
        self.history.insert(tk.END, '1st QUART of L  ' + str(self.x) + '\n')
        # set up for chain operation
        self.xFlag = True
        self.inxStr.focus()
        print("1st QUART of L")
        print("1st QUART of L is {}".format(self.x))
        
    def do_quartile3L(self):
        if not self.Lflag:
            self.arithmeticError()
            return
        # add variables entered together
        self.x =  np.percentile(self.L, 75)
        # log action to history 
        self.history.see(tk.END)
        # clear register before transferring result there
        if (len(self.inxStr.get())) > 0:
            self.inxStr.delete(0,tk.END)
        self.inxStr.insert(tk.INSERT, str(self.x))
        self.inLStr.insert(tk.INSERT, str(self.L))
        self.history.insert(tk.END, '3rd QUART of L  ' + str(self.x) + '\n')
        # set up for chain operation
        self.xFlag = True
        self.inxStr.focus()
        print("3rd QUART of L")
        print("3rd QUART of L is {}".format(self.x))
        
    def do_svTtestL(self):
        if not self.Lflag:
            self.arithmeticError()
            return
        # add variables entered together
        popmean =  st.mean(self.L)
        TP = stats.ttest_1samp(self.L, popmean)
        print(TP)
        # log action to history 
        self.history.see(tk.END)
        # clear register before transferring result there
        if (len(self.inxStr.get())) > 0:
            self.inxStr.delete(0,tk.END)
            print("cleared")
        self.inxStr.insert(tk.INSERT, str(TP))
        self.history.insert(tk.END, 'SVTtest of L  ' + str(TP) + '\n')
        # set up for chain operation
        self.xFlag = True
        self.inxStr.focus()
        print("SVTtestan L")
        print("SVTtest of L is {}".format(TP)) 
        
    def do_svZtestL(self):
        if not self.Lflag:
            self.arithmeticError()
            return
        # add variables entered together
        popmean =  st.mean(self.L)
        TP = stats.ttest_1samp(self.L, popmean)
        # log action to history 
        self.history.see(tk.END)
        # clear register before transferring result there
        if (len(self.inxStr.get())) > 0:
            self.inxStr.delete(0,tk.END)
            print("cleared")
        self.inxStr.insert(tk.INSERT, str(TP))
        self.history.insert(tk.END, 'SVTtest of L  ' + str(TP) + '\n')
        # set up for chain operation
        self.xFlag = True
        self.inxStr.focus()
        print("SVTtestan L")
        print("SVTtest of L is {}".format(TP)) 
        
    def do_CI95L(self):
        CI95 = stats.t.interval(0.95, len(self.L)-1, loc=np.mean(self.L), scale=stats.sem(self.L))
        self.history.see(tk.END)
        # clear register before transferring result there
        if (len(self.inxStr.get())) > 0:
            self.inxStr.delete(0,tk.END)
            print("cleared")
        self.inxStr.insert(tk.INSERT, str(CI95))
        self.history.insert(tk.END, 'SVTtest of L  ' + str(CI95) + '\n')
        # set up for chain operation
        self.xFlag = True
        self.inxStr.focus()
        print("SVTtestan L")
        print("SVTtest of L is {}".format(CI95))    
        
    def do_histoL(self):
        if not self.Lflag:
            self.arithmeticError()
            return
        # add variables entered together
        mu = st.mean(self.L)
        sigma = st.pstdev(self.L)
        # the histogram of the data
        n, bins, patches = plt.hist(self.L, 10, normed=1, facecolor='green', alpha=0.75)
        #best fit line
        y = mlab.normpdf( bins, mu, sigma)
        l = plt.plot(bins, y, 'r--', linewidth=1)
        plt.xlabel('Values')
        plt.ylabel('Probability')
        plt.title(r'Histogram of L:')
        plt.axis([0, 100, 0, 0.03])
        plt.grid(True)
        plt.show()
        
    def do_blank(self):
        # check for entered button
        if not self.xFlag:
            self.arithmeticError()
            return
        self.history.insert(tk.END, 'NOP  \n')
        self.history.see(tk.END)
        self.underConstruction()
        # do something else to (x)
        print('unused key')
        
    
    # Note pad Functions ###################################################
    '''
    Note Pad and History Implenetation Functions
    '''
        
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
        
    def do_save_note(self):
        notesFile = 'CalcNotes' + '.note'
        notesFolder = './notes/'
        if not path.exists(notesFolder):
            makedirs(notesFolder, exist_ok = True)
        openedFile = open(notesFolder + notesFile,"w")
        openedFile.write(self.scr_notes.get(1.0, tk.END) + '\n')
        openedFile.close()
        self.history.insert(tk.END, 'SAVED NOTES \n')
        self.history.see(tk.END)
        print("notes save finished")
        
    def do_load_note(self):
        print('Unable to Load notes, not implemented yet')
        self.underConstruction()
        
    # history functions ##################
           
    def do_clr_history(self, history):
        # clear the calculation history
        history.delete(1.0,tk.END)
        #self.history.insert(tk.END, 'CLEAR HISTORY\n')
        history.see(tk.END)
        print('cleared the history pad')
        
    def do_prt_history(self, history):
        print("\n History:\n")
        print(self.history.get(1.0, tk.END) + '\n')  # to Console
        self.history.insert(tk.END, 'PRINT NOTES \n')
        self.history.see(tk.END)
        self.historyToDialog()  # and show in a dialog
        
    def do_log_history(self):
        self.history.insert(tk.END, self.scr_notes.get(1.0, tk.END) + '\n')
        self.history.see(tk.END)
        
    def do_save_history(self):
        historyFile = 'CalcHistory' + '.hist'
        historyFolder = './history/'
        if not path.exists(historyFolder):
            makedirs(historyFolder, exist_ok = True)
        openedFile = open(historyFolder + historyFile,"w")
        openedFile.write(self.history.get(1.0, tk.END) + '\n')
        openedFile.close()
        self.history.insert(tk.END, 'SAVED HISTORY \n')
        self.history.see(tk.END)
        print("history save finished")
        
    
    # Menubar functions
    '''
    Menubar Function Implementations
    '''
        
    def do_toggleList(self):
        # toggle function flag
        if not self.Lflag:
            self.Lflag = True
        else:
            self.Lflag = False
        #now show appropriate flag
        if self.Lflag:
            self.xyFunctKeys.grid_forget()
            self.listFunctKeys.grid()
        else:
            self.listFunctKeys.grid_forget()
            self.listStatsKeys.grid_forget()
            self.xyFunctKeys.grid()
        print('switch function keys')
        
    

