from tkinter import *
from PIL import Image,ImageTk
tk = Tk()
tk.title("Tkinter Button Kullanımı")
tk.geometry("450x450")
tk.configure(bg="blue")
tk.resizable(width=False,height=False)

"""
Buton Fonksiyonları:

padx,pady = Butona yatay ve dikey olarak boyut vermemizi sağlar.
command = Butona tıklandığında yapılacak işlem atanır. Fonksiyon kullanır.
focus_set() = Buton odaklamasını sağlar.
cursor = fare imleci oluşturur.
activebackground = Butonun üzerine gelindiğinde buton rengini belirler.
activefontground = Butona tıklandığı anda rengini belirler.
state = Butonu aktif veya pasif yapmamızı sağlar.
image = Butona görsel ekler.

"""
def button1():
    lbl["text"] = "1. Butona Tıklandı"
def button2():
    lbl["text"] = "2. Butona Tıklandı"

btn = Button(tk,text="Buton1",padx=20,pady=5,command=button1).pack()
btn2 = Button(tk,text="Buton2",padx=10,pady=5,bg="red",fg="green",activebackground="yellow",activeforeground="purple",command=button2).pack()
lbl = Label(tk,bg="blue",fg="white")
lbl.pack()

resim = ImageTk.PhotoImage(Image.open("resim.png"))

btn3 = Button(tk,image=resim,compound="center",
            font="Verdana 12 bold",bg="red",fg="green",
            activebackground="black",activeforeground="yellow").pack()
tk.mainloop()