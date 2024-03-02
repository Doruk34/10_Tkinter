from tkinter import *

tk = Tk()
tk.title("Tkinter ListBox")
tk.geometry("450x450")
tk.resizable(width="False",height="False")

uygulama = Frame(tk,borderwidth=1,relief="solid")
uygulama.pack(anchor="ne")
Listbox1 = Listbox(uygulama,bg="yellow",fg="red",font="Verdana 12 bold",cursor="pirate")
Listbox1.insert(1,"Python")
Listbox1.insert(2,"C#")
Listbox1.insert(3,"Java")
Listbox1.insert(4,"Delphi")

Listbox1.grid(padx=15,pady=10)

tk.mainloop()

