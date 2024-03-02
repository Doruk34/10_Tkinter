from tkinter import *
from tkinter import ttk

tk = Tk()
tk.title("Sınıf ve Şube Seçimi")
tk.geometry("450x450")
tk.resizable(width=False,height=False)

def SinifSecildi():
    secilen_sinif = combo_var1.get()
    secilen_sube = combo_var2.get()

    sonuc = f"sinif:{secilen_sinif},şube:{secilen_sube}"
    label_sonuc.config(text=sonuc)

uygulama = Frame(tk)
uygulama.pack(pady=20)

veriler1 = ["9.Sınıf","10.Sınıf","11.Sınıf","12.Sınıf"]
veriler2 = ["A Şubesi","B Şubesi","C Şubesi","D Şubesi"]

combo_var1 = StringVar()
combo_var2 = StringVar()

Combo1 = ttk.Combobox(uygulama,values=veriler1,font="Verdana 12 bold",textvariable=combo_var1)
Combo1.set("Sınıfınızı Seçiniz")
Combo1.pack(pady=10)

Combo2 = ttk.Combobox(uygulama,values=veriler2,font="Verdana 12 bold",textvariable=combo_var2)
Combo2.set("Şube Seçiniz")
Combo2.pack(pady=10)

label_sonuc = Label(uygulama,text="Sınıf ve Şube Seç",font="Verdana 12 bold")
label_sonuc.pack()

button = Button(uygulama,text="Sınıf ve Şube Seç",font="Verdana 12 bold",command=SinifSecildi)
button.pack()

tk.mainloop()
