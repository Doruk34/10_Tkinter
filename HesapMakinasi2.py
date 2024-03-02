import tkinter as tk

def press_button(value):
    current_text = entry_display.get()
    entry_display.delete(0, tk.END)
    entry_display.insert(tk.END, current_text + str(value))

def clear_display():
    entry_display.delete(0, tk.END)

def calculate_result():
    try:
        expression = entry_display.get()
        result = eval(expression)
        entry_display.delete(0, tk.END)
        entry_display.insert(tk.END, str(result))
    except Exception as e:
        entry_display.delete(0, tk.END)
        entry_display.insert(tk.END, "Hata")

# Ana pencere oluştur
root = tk.Tk()
root.title("Hesap Makinesi")

# Giriş ekranı
entry_display = tk.Entry(root, width=20, font=('Arial', 14))
entry_display.grid(row=0, column=0, columnspan=4)

# Butonlar
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 14),
              command=lambda button=button: press_button(button) if button != '=' else calculate_result()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Temizleme düğmesi
tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 14), command=clear_display).grid(row=row_val, column=col_val, columnspan=2)

# Main loop
root.mainloop()
