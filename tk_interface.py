import tkinter as tk
import pandas as pd
import openpyxl
import datetime
import time

window = tk.Tk()
window.title("Warehouse Project")
frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
frm_form.pack()

labels = [
    "First Name:",
    "Last Name:",
    "Address Line 1:",
    "Address Line 2:",
    "City:",
    "State/Province:",
    "Postal Code:",
    "Country:",
]

for idx, text in enumerate(labels):
    label = tk.Label(master=frm_form, text=text)
    entry = tk.Entry(master=frm_form, width=50)
    label.grid(row=idx, column=0, sticky='e')
    entry.grid(row=idx, column=1)

frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

btn_submit = tk.Button(master=frm_buttons, text='Submit')
btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

btn_clear = tk.Button(master=frm_buttons, text="Clear")
btn_clear.pack(side=tk.RIGHT, ipadx=10)


def handle_keypress(event):
    print("The button was clicked")


btn_submit.bind('<Button-1>', handle_keypress)
btn_clear.bind('<Button-1>', handle_keypress)

if __name__ == '__main__':
    window.mainloop()
