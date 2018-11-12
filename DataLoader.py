'''
Created on Oct 2, 2018

@author: david
'''
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, simpledialog
import numpy as np
import pandas as pd
from DataSciCalc03 import L

active_Data_index = (9,)

class DatasetLoad(active_Dataset):
    '''
    This is a File access module for DataSciCalc
    '''
    active_Dataset = active_Dataset
    L = L
    arry = np.array(np.arange(10))
    S = pd.Series(L)
    dfT = pd.DataFrame()

    def __init__(self, params):
        '''
        Constructor
        '''
        
    def loadNewData(self, active_Dataset):
        '''
        Load New Data
        As list, numpy array, or as pandas dataframe as the case requires
        '''
        
class DatasetSelectDialog(simpledialog.Dialog):
    def __init__(self, parent):
        top = self.top = tk.Toplevel(parent)
        tk.Label(top, text="Choose Dataset").pack()
        self.e = tk.Listbox(top, height=3)
        self.e.pack(padx=5)
        for item in ["List L",  "Array arry", "Table dfTable", "Series S"]:
            self.e.insert(tk.END, item)
        self.e.update()
        b = tk.Button(top, text="OK", command=self.ok(self.e))
        b.pack()
        
        
    def ok(self):        
        self.top.destroy()
        


selindex = 0
root = tk.Tk()
tk.Button(root, text="Hello!").pack()
root.update()

d = DatasetSelectDialog(root)

root.wait_window(d.top)
root.mainloop()
print(d.e.curselection())    