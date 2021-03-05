import random
import tkinter as tk

def print_text():
    print(entry.get())

window = tk.Tk()
window.columnconfigure(0, minsize=150)
window.rowconfigure([0, 1], minsize=50)

entry = tk.Entry()
entry.pack()
btn_print = tk.Button(text="enter", command=print_text)
btn_print.pack()


window.mainloop()
