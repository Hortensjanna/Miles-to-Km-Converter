from tkinter import *


def convert():
    result_in_km = round(float(input_in_km.get()) * 1.609344, 2)
    result.config(text= result_in_km)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=290, height=100)
window.config(padx=35, pady=25)

button = Button(text="CONVERT",font=("Arial", 10, "normal"), command=convert)
button.grid(column=1, row=2)

input_in_km = Entry(width=10)
input_in_km.grid(column=1, row=0)

text_1 = Label(text="Miles", font=("Arial", 10, "normal"))
text_1.grid(column=2, row=0)

text_2 = Label(text="Km", font=("Arial", 10, "normal"))
text_2.grid(column=2, row=1)

text_3 = Label(text="is equal to", font=("Arial", 10, "normal"))
text_3.grid(column=0, row=1)

result = Label(text="0", font=("Arial", 10, "normal"))
result.grid(column=1, row=1)



window.mainloop()