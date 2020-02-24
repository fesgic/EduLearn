from idlelib.idle_test.mock_tk import Var
from tkinter import *
import mysql.connector as mariadb
import self
from pip._vendor.distlib import database

root = Tk()
root.geometry('500x500')
root.title("Registration Form")

surname = StringVar()
first = StringVar()
second = StringVar()
username = StringVar()
regno = StringVar()


def database():
   surname1=surname.get()
   first1=first.get()
   second1=second.get()
   username1=username.get()
   regno1=regno.get()
   mariadb_connection = mariadb.connect(user='root', password='fg68211h', database='edulearn')
   cursor = mariadb_connection.cursor()
   cursor=mariadb_connection.cursor()
   cursor.execute('INSERT INTO students (surname,first,second,username, regno) VALUES(%s,%s,%s,%s,%s)',(surname1,first1,second1,username1,regno1,))
   mariadb_connection.commit()
   mariadb_connection.close()

label_0 = Label(root, text="Registration form", width=20, font=("bold", 20))
label_0.place(x=90, y=53)

label_1 = Label(root, text="Surname", width=20, font=("bold", 10))
label_1.place(x=80, y=130)

entry_1 = Entry(root, textvar=surname)
entry_1.place(x=240, y=130)

label_2 = Label(root, text="First Name", width=20, font=("bold", 10))
label_2.place(x=68, y=180)

entry_2 = Entry(root, textvar=first)
entry_2.place(x=240, y=180)

label_3 = Label(root, text="Second Name", width=20, font=("bold", 10))
label_3.place(x=70, y=230)

entry_3 = Entry(root, textvar=second)
entry_3.place(x=240, y=230)

label_4 = Label(root, text="Username", width=20, font=("bold", 10))
label_4.place(x=70, y=280)

entry_4 = Entry(root, textvar=username)
entry_4.place(x=240, y=280)

label_5 = Label(root, text="Reg No", width=20, font=("bold", 10))
label_5.place(x=70, y=340)

entry_5 = Entry(root, textvar=regno)
entry_5.place(x=240, y=340)


Button(root, text='Submit', width=20, command=database, bg='brown',fg='white').place(x=180, y=390)

root.mainloop()
