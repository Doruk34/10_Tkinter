from tkinter import *

windows = Tk()
windows.title("RadioButton")
windows.geometry("400x200")
windows.resizable(width=False,height=False)

RadioVar = IntVar()
# RadioVar.set(3) Varsayılan seçim ataması yapar.

R1 = Radiobutton(windows,text="Kadın",variable=RadioVar,value=1).pack()

R2 = Radiobutton(windows,text="Erkek",variable=RadioVar,value=2).pack()

R3 = Radiobutton(windows,text="Belirtmek İstemiyorum",variable=RadioVar,value=3).pack()

windows.mainloop()