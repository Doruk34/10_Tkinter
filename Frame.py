from tkinter import *

anaPencere = Tk()
anaPencere.geometry("400x150")
cerceve1 = Frame(anaPencere,bg="red", cursor="star")
cerceve1.pack(side = "top")
cerceve2 = Frame(anaPencere,bg="blue")
cerceve2.pack(side = "bottom")
etiket1 = Label(cerceve1,bg="gray", text = "Merhaba Python Sevenler Derneği")
etiket1.pack(side=LEFT)
etiket2 = Label(cerceve1,bg="lightgreen", text = "Frame ( Çerçeve ) Örneği")
etiket2.pack(side=RIGHT)
etiket3 = Label(cerceve1,bg="lightblue", text = "BurasıÇerçeve :)")
etiket3.pack(side=BOTTOM)

dgm_kapat = Button(cerceve2, bg = "blue", fg = "white", width=12, text="Kapat", command=anaPencere.destroy)
dgm_kapat.pack(side = LEFT)
anaPencere.mainloop()