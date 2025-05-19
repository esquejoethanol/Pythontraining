import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style(root)
root.tk.call("source", "forest-dark.tcl")
style.theme_use("forest-dark")

frame = ttk.Frame(root)
frame.pack()

widgets_frame = ttk.LabelFrame(frame, text="insert row")
widgets_frame.grid(row=0,column=0)

name_entry = ttk.Entry(widgets_frame)
name_entry.insert(0, "Name")
name_entry.bind("<FocusIn>", lambda e: name_entry.delete('0','end'))
name_entry.grid(row=0, column=0, sticky="ew")

age_spinbox = ttk.Spinbox(widgets_frame, from_=18, to=100)
age_spinbox.insert(0,"Age")
age_spinbox.grid(row=1, column=0, sticky="ew")



root.mainloop