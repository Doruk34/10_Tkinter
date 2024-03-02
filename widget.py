
"""
Widget fonksyonları:

pack() = Pencerenin orta kısmından bölerek formu yukardan aşağıya doğru ekleme işlemi yapar.

grid() = Pencereye x ve y konumuna göre ekleme yapar. Satır sütün olarakta ekleme seçeneği sunar
    
row(0): satır eklemesi

column(): sütün eklemesi 

padx(): yatay eksende 

pady(): dikey eksende

place(): Konuma göre ekleme yapar x ve y konumu

"""
# Grid
from tkinter import *
def kordinat(a):
    x, y = a.x, a.y
    print(f"Fare Koordinatları: x={x}, y={y}")
tk = Tk()

tk.title("Widget Kullanımları")
tk.geometry("450x450")
G1 = Label(tk,text="Grid Label 1",font="Verdana 12 bold")
G1.grid(row=0,column=0,padx=5,pady=5)

Label(tk,text="Grid Label 2",font="Verdana 12 bold",bg="yellow").grid(row=0,column=1,padx=5,pady=5)

G3 = Label(tk,text="Grid Label 3",font="Verdana 12 bold",bg="red")
G3.grid(row=1,column=0,padx=5,pady=5)

G4 = Label(tk,text="Grid Label 4",font="Verdana 12 bold",bg="green")
G4.grid(row=1,column=1,padx=5,pady=5)

#Place

P1 = Label(tk,text="Place Label 1",font="Verdana 12 bold",bg="green")
P1.place(x=140,y=125)

yazi="Place Label 2"
yazi_uzunluk=len(yazi)
P2 = Label(tk,text=yazi,font="Verdana 12 bold",bg="blue")
P2.place(x=(450-yazi_uzunluk),y=(450-yazi_uzunluk))
tk.bind('<Motion>', kordinat)
tk.mainloop()
