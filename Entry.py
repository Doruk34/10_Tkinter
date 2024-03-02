from tkinter import *

tk = Tk()
tk.title("Tkinter Entry")
tk.geometry("350x350")
tk.resizable(width="False",height="False")

"""
Entry Fonksiyonları:
    with: Genişlik ayarlaması yapılır.
    show: Girilen verinin gizliliğini ayarlar.
    get: Verileri ekrana getirir. Çağırır.
    set: Verileri gönderir.
    insert: Verinin içerisine index veya indis numarasına göre ekleme yapar.
"""
lbl = Label(tk,text="Entry").pack()

entry1 = Entry(tk,width=25).pack()
entry2 = Entry(tk,textvariable=StringVar(),show="*",width=25).pack()

tk.mainloop()