'''
Created on Sep 30, 2018

@author: david
'''


import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, simpledialog, font
import os




class Dataset_wm(tk.Toplevel):
    def __init__(self):

        tk.Toplevel.__init__(self)        
        self.title('Select Dataset ...')
        
        # self.application_window = tk.Tk()
        # Variable
        
        # Functions
        
        
        def end():
            self.result=None
            self.destroy()
            
        # Main window Frame
        #=======================================================================
        # self.mainwindow=ttk.Frame(self)
        # self.mainwindow.pack(padx=10, pady=10)
        # # Main LabelFrame
        # self.mainframe=ttk.Frame(self.mainwindow)
        # self.mainframe.pack(side='top',ipady=30, ipadx=30,expand='no', fill='both')
        # self.mainframe0=ttk.Frame(self.mainwindow)
        # self.mainframe0.pack(side='top', expand='yes', fill='x', padx=10, pady=10)
        # self.mainframe1=ttk.Frame(self.mainwindow)
        # self.mainframe1.pack(side='top',expand='no', fill='both')
        # self.mainframe2=ttk.Frame(self.mainwindow)
        # self.mainframe2.pack(side='top',expand='yes', fill='x', padx=10, pady=10)
        #=======================================================================
        
        self.seldataset = ttk.LabelFrame(self, text=' Which Dataset to use ', width=40)
        self.seldataset.grid(column=0, row=0, sticky='W')
        MODES = [
        ("Current List", "L"),
        ("Current Dataframe", "df"),
        ("New Data", "new"),
        ("Clear All Data", "clrALL"),
        ]
        
        v = tk.StringVar()
        v.set("L") # initialize

        for text, mode in MODES:
            b = tk.Radiobutton(self, text=text, variable=v, value=mode )
            b.grid(padx=8,sticky='W')
            
        #=======================================================================
        # self.selList=ttk.Radiobutton(self, text='Current List', onvalue='bold', offvalue='normal', width=40, padx=8)
        # self.selList.grid(column=0, row=0)
        # self.selDataframe=ttk.Radiobutton(self, text='Current Dataframe', onvalue='italic', offvalue='roman', width=40, padx=8)
        # self.selDataframe.grid(column=0, row=1)
        # self.newData=ttk.Radiobutton(self, text='New Data Load',onvalue=1, offvalue=0, width=40, padx=8)
        # self.newData.grid(column=0, row=2)
        # self.clearAllData=ttk.Radiobutton(self, text='Clear All Data',onvalue=1, offvalue=0, width=40, padx=8)
        # self.clearAllData.grid(column=0, row=3)
        #=======================================================================

        
 
    
        self.mainloop()
        # Frame in [ 1. main frame]
        #=======================================================================
        # ttk.Entry(self.frame1, textvariable=self.var1).pack(side='top', padx=5, pady=5, expand='yes', fill='x')
        # self.size=tk.Listbox(self.frame1, bg='gray70')
        # self.size.pack(side='top', padx=5, pady=5, expand='yes', fill='both')
        # for i in range(30):
        #     self.size.insert(tk.END, i)
        #=======================================================================

#===============================================================================
#         tk.Label(self.mainframe1, bg='white',text=''' ABCDEabcde12345 ''', font=self.font_1).pack(expand='no', padx=10,pady=10)
# 
#         # Frame in [ 2. mainframe]
#         ttk.Button(self.mainframe2, text='   OK   ', command=out).pack(side='left', expand='yes', fill='x', padx=5, pady=5)
#         ttk.Button(self.mainframe2, text=' Cancel ', command=end).pack(side='left', expand='yes', fill='x', padx=5, pady=5)
#         ttk.Button(self.mainframe2, text=' Apply  ', command=applied).pack(side='left', expand='yes', fill='x', padx=5, pady=5)
#         
#         self.listbox.bind('<<ListboxSelect>>', checkface)
#         self.size.bind('<<ListboxSelect>>', checksize)
#         
#===============================================================================
#===============================================================================
# root = tk.Tk()
# font1=font.Font()
# tk.Text(root,font=font1).pack()
# Font_wm(Font=font1)
# root.mainloop()
#===============================================================================


Dataset_wm()
