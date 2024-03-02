from tkinter import *
from PIL import Image,ImageTk

tk = Tk()
tk.title("Tkinter Pillow")
tk.geometry("450x450")
tk.resizable(width=False,height=False)

# Görsel Ekleme
# resim = ImageTk.PhotoImage(Image.open("C:/Users/....../Downloads/gorsel.png"))
resim = ImageTk.PhotoImage(Image.open("gorsel.png"))
Label(tk,image=resim).pack()

# Orjinal Boyut
"""
resim2 = ImageTk.PhotoImage(Image.open("gorsel2.png"))
Label(tk,image=resim2).pack()

"""
# Resim boyutlandırma
resim3 = Image.open("gorsel2.png")
resim_boyutlandirma = resim3.resize((100,100))
boyutlama = ImageTk.PhotoImage(resim_boyutlandirma)
Label(tk,image=boyutlama).pack()
tk.mainloop()