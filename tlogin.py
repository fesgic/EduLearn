from tkinter import *
from functools import partial


def validateLogin(username, password):
    print("username entered :", username.get())
    print("password entered :", password.get())
    return

# window
tkWindow = Tk()
tkWindow.geometry('400x300')
tkWindow.title('EduLearn')

# username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=3, column=2)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=3, column=5)

# password label and password entry box
passwordLabel = Label(tkWindow, text="Password").grid(row=5, column=2)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=5, column=5)

validateLogin = partial(validateLogin, username, password)

# login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=6, column=5)

tkWindow.mainloop()
