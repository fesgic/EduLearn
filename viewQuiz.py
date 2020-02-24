from idlelib.idle_test.mock_tk import Var
from tkinter import *
import mysql.connector as mariadb
import self
from pip._vendor.distlib import database

root = Tk()
root.geometry('500x500')
root.title("Set Test")

test = StringVar()
quiz = StringVar()
ans1 = StringVar()
ans2 = StringVar()
ans3 = StringVar()
correct = StringVar()

def database():
   label_1=test.get()
   label_2=quiz.get()
   label_3=ans1.get()
   label_4=ans2.get()
   label_5=ans3.get()
   mariadb_connection = mariadb.connect(user='root', password='fg68211h', database='edulearn')
   cursor = mariadb_connection.cursor()
   cursor=mariadb_connection.cursor()
   cursor.execute('SELECT * from quiz (test,quiz,ans1,ans2,ans3) VALUES(%s,%s,%s,%s,%s)',(label_1,label_2,label_3,label_4,label_5))
   mariadb_connection.fetchall().grid(row=5,column=5)
   mariadb_connection.close()

label_1 = Label(root, text="Test")
label_1.grid(row=3, column=0)

label_2 = Label(root, text="Question")
label_2.grid(row=5, column=0)

label_3 = Label(root, text="Answer1")
label_3.grid(row=7, column=0)

label_4 = Label(root, text="Answer2")
label_4.grid(row=9, column=0)

label_5 = Label(root, text="Answer3")
label_5.grid(row=11, column=0)

text = Text(root, height=10, width=24)
text.grid(row=4, columnspan=2)
text.insert(END, command=database())



root.mainloop()
