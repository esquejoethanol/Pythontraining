import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.tk.call("source")
root.tk.call("source")
style.theme_use()

frame = ttk.Frame(root)
frame.pack()

widgets_frame = ttk.LabelFrame(frame, text="insert Row")
widgets_frane.grid(row=0, column=0)

name_entry = ttk.Entry(widgets_frame)
name_entry.insert(0,"name")
name_entry.grid(row=0, column=0, sticky="eastwest")


root.mainloop()