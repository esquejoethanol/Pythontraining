import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title("Login Form")
window.geometry('440x320')
window.configure(bg='#333333')

def login():
    username = "admin"
    password = "admin1"
    if user_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login", message="Login Success")
    else:
        messagebox.showwarning(title="Error", message="Login Failed")

frame = tkinter.Frame(bg='#333333')

login_label = tkinter.Label(frame, text="Login", bg='#333333', fg='white')
user_label = tkinter.Label(frame, text="username", bg='#333333', fg='white')
user_entry = tkinter.Entry(frame)
password_entry = tkinter.Entry(frame, show="****")
password_label = tkinter.Label(frame, text="Password", bg='#333333', fg='white')
login_button = tkinter.Button(frame, text="login", bg='orange', fg='black', command=login)

login_label.grid(row=0, column=1, columnspan=2, sticky='news', pady='30')
user_label.grid(row=1, column=0)
user_entry.grid(row=1, column=1, pady='10')
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1)
login_button.grid(row=3, column=1, columnspan=2, pady='30')

frame.pack()

window.mainloop()