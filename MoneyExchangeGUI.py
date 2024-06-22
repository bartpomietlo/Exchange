from MoneyExchange import get_currency, curr
from customtkinter import *


set_appearance_mode("dark")
set_default_color_theme("dark-blue")
root = CTk()
root.geometry("500x400")
root.title("Currency Exchange")
frame = CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill='both', expand=True)

label = CTkLabel(master=frame, text="Exchange")
label.pack(pady=10, padx=10)

def waluta(*args):
    try:
        text = entry1_var.get()
        if text:
            input_currency = input_currency_var.get()
            output_currency = output_currency_var.get()
            money = get_currency(input_currency, output_currency)[0] * float(text)
            entry2_var.set(f'{money:.2f} {curr[output_currency][1]}')
        else:
            entry2_var.set('')
    except Exception:
        entry2_var.set(f'{float(text)} {curr[output_currency][1]}')

input_currency_var = StringVar(value='zloty')
output_currency_var = StringVar(value='dinar')

input_currency_menu = CTkOptionMenu(master=frame, variable=input_currency_var, values=list(curr.keys()), command=waluta)
input_currency_menu.pack(pady=10, padx=10)

entry1_var = StringVar()
entry1_var.trace("w", waluta)

entry1 = CTkEntry(master=frame, placeholder_text='Amount', textvariable=entry1_var)
entry1.pack(pady=20, padx=20)

output_currency_menu = CTkOptionMenu(master=frame, variable=output_currency_var, values=list(curr.keys()), command=waluta)
output_currency_menu.pack(pady=10, padx=10)

entry2_var = StringVar()
entry2 = CTkEntry(master=frame, placeholder_text='Result', textvariable=entry2_var, state='readonly')
entry2.pack(pady=20, padx=20)

root.mainloop()
