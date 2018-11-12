'''
test code class
Created on Nov 6, 2018

@author: david
'''
'''
Created on Sep 30, 2018

@author: david
'''
from tkinter import *
import pandas as pd 
from pandastable import Table




from tkinter import *
from pandastable import Table, TableModel
 
class TestApp(Frame):
    """Basic test frame for the table"""
    def __init__(self, parent=None):
        self.parent = parent
        Frame.__init__(self)
        self.main = self.master
        self.main.geometry('600x400+200+100')
        self.main.title('Table app')
        f = Frame(self.main)
        f.pack(fill=BOTH,expand=1)
        #df = TableModel.getSampleData()
        df = pd.read_csv('co2.csv')
        pt = Table(f, dataframe=df,
                                showtoolbar=True, showstatusbar=True)
        pt.show()
        return
 
app = TestApp()
#launch the app
app.mainloop()
