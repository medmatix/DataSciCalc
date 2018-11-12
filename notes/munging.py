'''
Created on Nov 8, 2018

@author: david
'''
# #####################################
#  imports
# #####################################
from tkinter import filedialog, simpledialog, messagebox as mBox
import os
import sys as sys
import csv
import time
from datetime import datetime
import math
import numpy as np
import pandas as pd
from scipy import stats

class Munging(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
    
    def pdSeriesfrList(self, L):
        pdSeries = pd.Series(data=L, index=None, dtype=None, name=None, copy=False, fastpath=False)  
        return pdSeries
    
    def listfrSeries(self, pdSeries):
        L = pdSeries.tolist()
        return L
    
    def getFileInfo(self):
        #Build a list of tuples for each file type the file dialog should display
        my_filetypes = [('all files', '.*'), ('text files', '.txt'), ('comma separated', ".csv"), ('MS Excel ', ".xlt")]
        answer = filedialog.askopenfilename(parent=self.win, initialdir=os.getcwd(), title="Please select a file:", filetypes=my_filetypes)
        fh = open(answer, 'r')
        fline = fh.readline()
        fh.close()
        numVar = len(fline.split(','))
        mBox.showinfo('Variable Count in csv file', 'The number of variables is: {}'.format(numVar))
        
