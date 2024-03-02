from tkinter import *
from tkinter import ttk

tk = Tk()
tk.title("Tkinter ComboBox Kullanımı")
tk.geometry("450x450")
tk.resizable(width=False,height=False)
uygulama = Frame(tk)
uygulama.pack()
veriler = ["9.Sınıf","10.Sınıf","11.Sınıf","12.Sınıf"]
Combo = ttk.Combobox(uygulama,values=veriler)
Combo.set("Sınıfınızı Seçiniz")
Combo.pack(padx=5,pady=5)
tk.mainloop()



