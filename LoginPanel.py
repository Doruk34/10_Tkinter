from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

window = Tk()
window.title("Kullanıcı Giriş Paneli")

window.geometry("560x512+600+300")
window.resizable(width="False",height="False")

window.iconbitmap("loginico.ico")

resim = ImageTk.PhotoImage(Image.open("resimlogin2.png"))
lresim = Label(window,image=resim)
lresim.place(x=20,y=10)

L3 = Label(window)
L3.place(x=350,y=400)

def giris():
    if(E1.get()==str("admin") and E2.get()==str("Aa1234")):
        L3["text"] = ("Giriş Başarılı!")
        messagebox.showinfo("Oturum","Giriş Başarılı!")
        print("Giriş Başarılı!")
        window2 = Tk()
        window2.title("AnaSayfa")
        window2.geometry("400x200+600+300")
        window2.resizable(width="False",height="False")
        window2.iconbitmap("home.ico")
        window2.mainloop()
    else:
        L3["text"] = ("Hatalı Giriş!")
        messagebox.showerror("Oturum","Giriş Başarısız!")
        print("Hatalı Giriş!")

L1 = Label(window,text="Kullanıcı Adı",font="Verdana 8 bold")
L1.place(x=240,y=271)

E1 = Entry(window,font="Verdana 8 bold")
E1.place(x=330,y=271,height=25,width=170)

L2 = Label(window,text="Şifre",font="Verdana 8 bold")
L2.place(x=240,y=320)

E2 = Entry(window,show="*",font="Verdana 8 bold")
E2.place(x=330,y=315,height=25,width=170)

bt = Button(window,text="Giriş Yap",bg="pink",fg="black",font="Verdana 8 bold",padx="5",pady="10",command=giris)
bt.place(x=350,y=350)

window.mainloop()