from tkinter import *

tk = Tk()
tk.title("Pyhon İle Tkinter")
tk.geometry("450x450")
tk.resizable(width=False,height=False)


"""
Label Fonksiyonu:

text = Yazılmak istenilen metin buraya yazılır.
font = Yazı tipi boyut veya biçimi.
bg = Arkaplan renklendirmesi.
bold = Kalın yazma.
underline = Altı çizili metin yazma.
bds = Yazı kenar boşlukları varsayılan 2px olarak verir.

"""
Label(tk,text="PYTHON",font="Verdana 12",bg="red",fg="yellow").pack()
Label(tk,text="python",font="Verdana 12 bold italic underline",bg="blue",fg="yellow").pack()
Label(tk,text="Tkinter",font="Gothic 12 bold italic underline",bg="blue",fg="yellow").pack()
tk.mainloop()