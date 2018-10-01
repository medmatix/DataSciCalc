'''
Created on Sep 30, 2018

@author: david
'''
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, simpledialog, font
import os

#===============================================================================
# try:
#     import tkinterex
# except:
#     import tkinter as tk 
#===============================================================================

application_window = tk.Tk()

#===============================================================================
# # Build a list of tuples for each file type the file dialog should display
# my_filetypes = [('all files', '.*'), ('text files', '.txt')]
# 
# # Ask the user to select a folder.
# answer = filedialog.askdirectory(parent=application_window,
#                                  initialdir=os.getcwd(),
#                                  title="Please select a folder:")
# 
# # Ask the user to select a single file name.
# answer = filedialog.askopenfilename(parent=application_window,
#                                     initialdir=os.getcwd(),
#                                     title="Please select a file:",
#                                     filetypes=my_filetypes)
# 
# # Ask the user to select a one or more file names.
# answer = filedialog.askopenfilenames(parent=application_window,
#                                      initialdir=os.getcwd(),
#                                      title="Please select one or more files:",
#                                      filetypes=my_filetypes)
# 
# # Ask the user to select a single file name for saving.
# answer = filedialog.asksaveasfilename(parent=application_window,
#                                       initialdir=os.getcwd(),
#                                       title="Please select a file name for saving:",
#                                       filetypes=my_filetypes)
#===============================================================================




#===============================================================================
# answer = simpledialog.askstring("Input", "What is your first name?",
#                                 parent=application_window)
# if answer is not None:
#     print("Your first name is ", answer)
# else:
#     print("You don't have a first name?")
# 
# answer = simpledialog.askinteger("Input", "What is your age?",
#                                  parent=application_window,
#                                  minvalue=0, maxvalue=100)
# if answer is not None:
#     print("Your age is ", answer)
# else:
#     print("You don't have an age?")
# 
# answer = simpledialog.askfloat("Input", "What is your salary?",
#                                parent=application_window,
#                                minvalue=0.0, maxvalue=100000.0)
# if answer is not None:
#     print("Your salary is ", answer)
# else:
#     print("You don't have a salary?")
#     
# if __name__ == '__main__':
#     pass
#===============================================================================

class Font_wm(tk.Toplevel):
    def __init__(self, Font=None):

        tk.Toplevel.__init__(self)
        self.mainfont=Font
        self.title('Font ...')

        # Variable
        self.var=tk.StringVar()# For Font Face
        self.var.set(self.mainfont.actual('family'))
        self.var1=tk.IntVar()  # for Font Size
        self.var1.set(self.mainfont.actual('size'))
        self.var2=tk.StringVar() # For Bold
        self.var2.set(self.mainfont.actual('weight'))
        self.var3=tk.StringVar() # For Italic
        self.var3.set(self.mainfont.actual('slant'))
        self.var4=tk.IntVar()# For Underline
        self.var4.set(self.mainfont.actual('underline'))
        self.var5=tk.IntVar() # For Overstrike
        self.var5.set(self.mainfont.actual('overstrike'))


        # Font Sample
        self.font_1=font.Font()
        for i in ['family', 'weight', 'slant', 'overstrike', 'underline', 'size']:
            self.font_1[i]=self.mainfont.actual(i)

        # Function
        def checkface(event):
            try:
                self.var.set(str(self.listbox.get(self.listbox.curselection())))
                self.font_1.config(family=self.var.get(), size=self.var1.get(), weight=self.var2.get(), slant=self.var3.get(), underline=self.var4.get(), overstrike=self.var5.get())
            except:
               pass
        def checksize(event):
            try:
                self.var1.set(int(self.size.get(self.size.curselection())))
                self.font_1.config(family=self.var.get(), size=self.var1.get(), weight=self.var2.get(), slant=self.var3.get(), underline=self.var4.get(), overstrike=self.var5.get())
            except:
                pass            
        def applied():
            self.result=(self.var.get(), self.var1.get(), self.var2.get(), self.var3.get(), self.var4.get(), self.var5.get())
            self.mainfont['family']=self.var.get()
            self.mainfont['size']=self.var1.get()
            self.mainfont['weight']=self.var2.get()
            self.mainfont['slant']=self.var3.get()
            self.mainfont['underline']=self.var4.get()
            self.mainfont['overstrike']=self.var5.get()
        def out():
            self.result=(self.var.get(), self.var1.get(), self.var2.get(), self.var3.get(), self.var4.get(), self.var5.get())
            self.mainfont['family']=self.var.get()
            self.mainfont['size']=self.var1.get()
            self.mainfont['weight']=self.var2.get()
            self.mainfont['slant']=self.var3.get()
            self.mainfont['underline']=self.var4.get()
            self.mainfont['overstrike']=self.var5.get()
            self.destroy()
        def end():
            self.result=None
            self.destroy()
            
        # Main window Frame
        self.mainwindow=ttk.Frame(self)
        self.mainwindow.pack(padx=10, pady=10)
        # Main LabelFrame
        self.mainframe=ttk.Frame(self.mainwindow)
        self.mainframe.pack(side='top',ipady=30, ipadx=30,expand='no', fill='both')
        self.mainframe0=ttk.Frame(self.mainwindow)
        self.mainframe0.pack(side='top', expand='yes', fill='x', padx=10, pady=10)
        self.mainframe1=ttk.Frame(self.mainwindow)
        self.mainframe1.pack(side='top',expand='no', fill='both')
        self.mainframe2=ttk.Frame(self.mainwindow)
        self.mainframe2.pack(side='top',expand='yes', fill='x', padx=10, pady=10)
        # Frame in [  main frame]
        self.frame=ttk.LabelFrame(self.mainframe, text='Select Font Face')
        self.frame.pack(side='left', padx=10, pady=10, ipadx=20, ipady=20, expand='yes', fill='both')
        self.frame1=ttk.LabelFrame(self.mainframe, text='Select Font size')
        self.frame1.pack(side='left', padx=10, pady=10, ipadx=20, ipady=20, expand='yes', fill='both')
        ttk.Entry(self.frame, textvariable=self.var).pack(side='top', padx=5, pady=5, expand='yes', fill='x')
        self.listbox=tk.Listbox(self.frame, bg='gray70')
        self.listbox.pack(side='top', padx=5, pady=5, expand='yes', fill='both')
        for i in font.families():
            self.listbox.insert(tk.END, i)

        # Frame in [ 0. mainframe]
        self.bold=ttk.Checkbutton(self.mainframe0, text='Bold', onvalue='bold', offvalue='normal', variable=self.var2)
        self.bold.pack(side='left',expand='yes', fill='x')
        self.italic=ttk.Checkbutton(self.mainframe0, text='Italic', onvalue='italic', offvalue='roman',variable=self.var3)
        self.italic.pack(side='left', expand='yes', fill='x')
        self.underline=ttk.Checkbutton(self.mainframe0, text='Underline',onvalue=1, offvalue=0, variable=self.var4)
        self.underline.pack(side='left', expand='yes', fill='x')
        self.overstrike=ttk.Checkbutton(self.mainframe0, text='Overstrike',onvalue=1, offvalue=0, variable=self.var5)
        self.overstrike.pack(side='left', expand='yes', fill='x')
        
        # Frame in [ 1. main frame]
        ttk.Entry(self.frame1, textvariable=self.var1).pack(side='top', padx=5, pady=5, expand='yes', fill='x')
        self.size=tk.Listbox(self.frame1, bg='gray70')
        self.size.pack(side='top', padx=5, pady=5, expand='yes', fill='both')
        for i in range(30):
            self.size.insert(tk.END, i)

        tk.Label(self.mainframe1, bg='white',text='''
ABCDEabcde12345
''', font=self.font_1).pack(expand='no', padx=10,pady=10)

        # Frame in [ 2. mainframe]
        ttk.Button(self.mainframe2, text='   OK   ', command=out).pack(side='left', expand='yes', fill='x', padx=5, pady=5)
        ttk.Button(self.mainframe2, text=' Cancel ', command=end).pack(side='left', expand='yes', fill='x', padx=5, pady=5)
        ttk.Button(self.mainframe2, text=' Apply  ', command=applied).pack(side='left', expand='yes', fill='x', padx=5, pady=5)
        
        self.listbox.bind('<<ListboxSelect>>', checkface)
        self.size.bind('<<ListboxSelect>>', checksize)
        
root = tk.Tk()
font1=font.Font()
tk.Text(root,font=font1).pack()
Font_wm(Font=font1)

root.mainloop()