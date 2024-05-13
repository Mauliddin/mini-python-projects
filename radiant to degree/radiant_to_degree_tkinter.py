from tkinter import Tk, Label, Entry, Button
import math

def convert(number):
    return round(number * (180/math.pi), 2)

def on_click():
    radiant_value = int(radiant_entry.get())
    degree_value = convert(radiant_value)
    degree_number.config(text=f"{degree_value}")
    
window = Tk()
window.config(padx=50, pady=20)
window.title("Radiant to degree")

radiant_label = Label(text="Radiant")
radiant_entry = Entry(width=20)
radiant_entry.focus()
degree_label = Label(text="Degree")
degree_number = Label(text="0")
in_label = Label(text="in")
convert_btn = Button(text="Convert", width=18, command=on_click)

radiant_label.grid(row=0, column=2)
radiant_entry.grid(row=0, column=1)
in_label.grid(row=1,column=0)
degree_number.grid(row=1, column=1)
degree_label.grid(row=1, column=2)
convert_btn.grid(row=2, column=1)


window.mainloop()