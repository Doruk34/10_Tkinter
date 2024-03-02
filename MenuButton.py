from tkinter import *

tk = Tk()
tk.title("Tkinter Menü Buton")
tk.geometry("450x450")
tk.resizable(width="False",height="False")

MB = Menubutton(tk,text="Menü",relief=RAISED)
MB.grid()

MB.menu = Menu(MB,tearoff=0)
MB["menu"] = MB.menu
var1 = IntVar()
var2 = IntVar()

MB.menu.add_checkbutton(label="tes1",variable=var1)
MB.menu.add_checkbutton(label="tes2",variable=var2)

MB.pack

tk.mainloop()