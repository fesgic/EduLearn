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
   test1=test.get()
   quiz1=quiz.get()
   ans11=ans1.get()
   ans22=ans2.get()
   ans33=ans3.get()
   correct1=correct.get()
   mariadb_connection = mariadb.connect(user='root', password='fg68211h', database='edulearn')
   cursor = mariadb_connection.cursor()
   cursor=mariadb_connection.cursor()
   cursor.execute('INSERT INTO quiz (test,quiz,ans1,ans2,ans3,correct) VALUES(%s,%s,%s,%s,%s,%s)',(test1,quiz1,ans11,ans22,ans33,correct1))
   mariadb_connection.commit()
   mariadb_connection.close()

label_0 = Label(root, text="Set Test", width=20, font=("bold", 20))
label_0.place(x=90, y=53)

label_1 = Label(root, text="Test Name", width=20, font=("bold", 10))
label_1.place(x=80, y=130)

entry_1 = Entry(root, textvar=test)
entry_1.place(x=240, y=130)

label_2 = Label(root, text="Question", width=20, font=("bold", 10))
label_2.place(x=68, y=180)

entry_2 = Entry(root, textvar=quiz)
entry_2.place(x=240, y=180)

label_3 = Label(root, text="answer 1", width=20, font=("bold", 10))
label_3.place(x=70, y=230)

entry_3 = Entry(root, textvar=ans1)
entry_3.place(x=240, y=230)

label_4 = Label(root, text="Answer 2", width=20, font=("bold", 10))
label_4.place(x=70, y=280)

entry_4 = Entry(root, textvar=ans2)
entry_4.place(x=240, y=280)

label_5 = Label(root, text="Answer 3", width=20, font=("bold", 10))
label_5.place(x=70, y=340)

entry_5 = Entry(root, textvar=ans3)
entry_5.place(x=240, y=340)

label_6 = Label(root, text="Answer 3", width=20, font=("bold", 10))
label_6.place(x=70, y=380)

entry_6 = Entry(root, textvar=correct)
entry_6.place(x=240, y=380)


Button(root, text='Submit', width=20, command=database, bg='brown',fg='white').place(x=180, y=420)

root.mainloop()
