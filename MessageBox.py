from tkinter import *
from tkinter import messagebox

tk = Tk()
tk.title("Tkinter Messagebox Buton")
tk.geometry("450x450")
tk.resizable(width="False",height="False")
"""
MessageBox Fonksiyonları
Bilgi, Hata ve Uyarı olmak üzere 3'e ayrılır:

showinfo
showerror
showwarning

Hata Butonları:

askyesno
askokcancel
askquestion
askreadycancel
asknocancel

"""
def show():
    messagebox.showinfo("Bilgi","İçerik")
    messagebox.showerror("Hata","İçerik")
    messagebox.showwarning("Uyarı","İçerik")

def ask():
    messagebox.askokcancel("Başlık","İçerik")
    messagebox.askquestion("Başlık","İçerik")
    messagebox.askretrycancel("Başlık","İçerik")
    messagebox.askyesno("Başlık","İçerik")
    messagebox.askyesnocancel("Başlık","İçerik")

L1 = Label(tk,text="MessageBox", font="Verdana 12 bold").pack()

B1 = Button(tk,text="Show",command=show).pack()
B2 = Button(tk,text="Ask",command=ask).pack()

tk.mainloop()