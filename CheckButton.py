from tkinter import *

root = Tk()
root.title("CheckButton Kullanımı")
root.geometry("450x450")

CheckVar1 = IntVar()
CheckVar2 = IntVar()
cerceve = Frame(bg="red").pack
Checkbutton1 = Checkbutton(root,text="Elma",variable=CheckVar1,
                         onvalue=1,offvalue=0,height=5,
                         width=10).pack()
Checkbutton2 = Checkbutton(root,text="Armut",variable=CheckVar2,
                         onvalue=1,offvalue=0,height=5,
                         width=10).pack()
root.mainloop()


