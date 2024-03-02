from tkinter import *


root = Tk() 
root.geometry("400x400") 
root.title('Menu Demonstration') 
menubar = Menu(root) 

file = Menu(menubar, tearoff=0) 
menubar.add_cascade(label='File', menu=file) 
file.add_command(label='New File') 
file.add_command(label='Open...') 
file.add_command(label='Save') 

edit = Menu(menubar, tearoff=0) 
menubar.add_cascade(label='Edit', menu=edit) 
edit.add_command(label='Cut') 
edit.add_command(label='Copy') 
edit.add_command(label='Paste') 
edit.add_command(label='Select All') 

help_ = Menu(menubar, tearoff=0) 
menubar.add_cascade(label='Help', menu=help_) 
help_.add_command(label='Tk Help') 
help_.add_command(label='Demo') 

root.config(menu=menubar) 

root.mainloop() 
