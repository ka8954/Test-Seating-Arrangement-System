import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox

root = Tk()
root.title("TEST SEATING")

connection = mysql.connector.connect(host='localhost', user='root', password='dbmsproject',port='3306', database='new_schema')
c = connection.cursor()

bkg = "#636e72"


frame = tk.Frame(root, bg=bkg)

label_firstname = tk.Label(frame, text="ID : ", font=('verdana',12), bg=bkg)
entry_firstname = tk.Entry(frame, font=('verdana',12))

label_lastname = tk.Label(frame, text="USERNAME : ", font=('verdana',12), bg=bkg)
entry_lastname = tk.Entry(frame, font=('verdana',12))

label_email = tk.Label(frame, text="PASSWORD : ", font=('verdana',12), bg=bkg)
entry_email = tk.Entry(frame, font=('verdana',12))



def insertData():
    firstname = entry_firstname.get()
    lastname = entry_lastname.get()
    email = entry_email.get()
    labcapacity = 50

    a = 1
    x = [i for i in range(a, labcapacity+1)]
    random.shuffle(x)

    for i in range(0, 50):
        seat = x[i]

    insert_query = "INSERT INTO new (ID, Username, Password, Sysno) VALUES(%s,%s,%s,%s)"
    vals = (firstname, lastname, email, seat)
    c.execute(insert_query,vals)
    connection.commit()
    res = seat
    messagebox.showinfo("YOUR SEAT NO", seat)



button_insert = tk.Button(frame, text="Insert", font=('verdana',14), bg='orange',command = insertData)

label_firstname.grid(row=0, column=0)
entry_firstname.grid(row=0, column=1, pady=10, padx=10)

label_lastname.grid(row=1, column=0)
entry_lastname.grid(row=1, column=1, pady=10, padx=10)

label_email.grid(row=2, column=0, sticky='e')
entry_email.grid(row=2, column=1, pady=10, padx=10)


button_insert.grid(row=4,column=0, columnspan=2, pady=10, padx=10, sticky='nsew')

frame.grid(row=0, column=0)


root.mainloop()
