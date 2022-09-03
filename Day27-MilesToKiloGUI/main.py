from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=300, height=200)
window.config(padx=50, pady=100)

fixed_term1 = Label(text="Miles")
fixed_term1.grid(row=0, column=2)
fixed_term2 = Label(text="is equal to")
fixed_term2.grid(row=1, column=0)
fixed_term3 = Label(text="Km")
fixed_term3.grid(row=1, column=2)

converted_value = Label(text="0")
converted_value.grid(row=1, column=1)


def button_click():
    mile_value = float(input_value.get())
    km_value = str(mile_value*1.609344)
    converted_value.config(text=km_value)


button1 = Button(text="Calculate", command=button_click)
button1.grid(row=2, column=1)

input_value = Entry(width=10)
input_value.grid(row=0, column=1)

window.mainloop()