# Creating GUI's using TKinter
"""Since we are using multiple modules from tkinter, we are importing everything into it
so we dont have to type tkinter everytime"""

from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=150, height=150)
window.config(padx=50, pady=50)

#Label

my_label1 = Label(text="is equal to", font=("Arial", 10, "normal"))
my_label1.grid(column=0, row=1)

my_label2 = Label(text="Miles", font=("Arial", 10, "normal"))
my_label2.grid(column=2, row=0)

my_label3 = Label(text="Km", font=("Arial", 10, "normal"))
my_label3.grid(column=2, row=1)

value_label = Label(text="0", font=("Arial", 10, "normal"))
value_label.grid(column=1, row=1)

#Button
def button_clicked():
    new_text = u_input.get()
    km_value = int(new_text)*1.609
    value_label.config(text=km_value)


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)



# Entry

u_input = Entry(width=10)
u_input.grid(column=1, row=0)



window.mainloop()
