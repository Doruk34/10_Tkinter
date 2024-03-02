from tkinter import *
from PIL import Image, ImageTk

tk = Tk()
tk.title("Tkinter Pillow")
tk.geometry("450x400")
tk.resizable(width=True, height=True)  # Boyutlandırmaya izin ver

# Çerçeve görüntüsünü ekleme

cerceve_resmi = ImageTk.PhotoImage(Image.open("gorsel.png"))
cerceve_etiketi = Label(tk, image=cerceve_resmi)
cerceve_etiketi.pack()

# Resmi boyutlandırma
png_resmi = Image.open("gorsel2.png")
yeniden_boyutlandirilmis_png_resmi = png_resmi.resize((100, 60))

yeniden_boyutlandirilmis_png_resmi_etiketi = ImageTk.PhotoImage(yeniden_boyutlandirilmis_png_resmi)
png_etiketi = Label(tk, image=yeniden_boyutlandirilmis_png_resmi_etiketi)
png_etiketi.pack()

# Çerçeveyle birlikte PNG resminin boyutunu güncellemek için fonksiyon
def boyutu_guncelle(x):
    yeni_genislik = x.width
    yeni_yukseklik = int(yeni_genislik *0.6)  # Orijinal PNG resminin en-boy oranını koru
    yeniden_boyutlandirilmis_resim = png_resmi.resize((yeni_genislik, yeni_yukseklik))
    yeni_png_etiketi_resmi = ImageTk.PhotoImage(yeniden_boyutlandirilmis_resim)
    png_etiketi.config(image=yeni_png_etiketi_resmi)
    png_etiketi.image = yeni_png_etiketi_resmi  # Çöp toplama önlemek için referansı güncelle

# Boyut değişiklik olayını fonksiyonla ilişkilendirmek
tk.bind("<Configure>", boyutu_guncelle)

tk.mainloop()
