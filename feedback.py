import tkinter as tk
import mysql.connector as mysql
from tkinter import *


root2 = Tk()
root2.title = "FEEDBACK"
root2.geometry("510x630")

con = mysql.connect(host='localhost', user='root', password='', port='3306', database='feedback')
global bc
bc = con.cursor()

lab=tk.Label(root2, text="User Feed Back Form", font=("Arial", 16), fg='#007acc')
lab.place(x=10, y=5)

fback1=tk.Label(root2, text="Please fill out the form so we could deliver a better experience for the users.", font=("Arial",11),)
fback1.place(x=10, y=30)

fback2 = tk.Label(root2, text="Thank you!!! ⊂(´・ω・｀⊂)", font=("Arial", 14))
fback2.place(x=130, y=590)

fback3 = tk.Label(root2, text="email", font=("Arial", 11))
fback3.place(x=20, y=70)

global mail
mail = tk.Entry(root2)
mail.place(height=20, width=170, x=20, y=90)

fback4 = tk.Label(root2, text="name", font=("Arial", 11))
fback4.place(x=320, y=70)

global namae
namae = tk.Entry(root2)
namae.place(height=20, width=170, x=320, y=90)

fback5 = tk.Label(root2, text="What is your experience when using this app?", font=("Arial", 11))
fback5.place(x=105, y=150)

global exp
exp = tk.Text(root2)
exp.place(height=80, width=300, x=105, y=170)

fback6 = tk.Label(root2, text="What can you recommend to make this app better?", font=("Arial", 11))
fback6.place(x=90, y=290)

global rec
rec = tk.Text(root2)
rec.place(height=80, width=335, x=90, y=310)

fback7 = tk.Label(root2, text="How would you rate this app?", font=("Arial", 11))
fback7.place(x=160, y=435)

global GRYaris
GRYaris = IntVar()

def submit():
    a = mail.get()
    b = namae.get()
    c = exp.get('1.0','end')
    d = rec.get('1.0','end')
    e = GRYaris.get()

    nissan = "INSERT INTO `fb`(`email`, `name`, `experience`, `recommendation`, `rating` ) VALUES (%s, %s, %s, %s, %s)"
    gtr_r34 = (a,b,c,d,e)
    bc.execute(nissan, gtr_r34)
    con.commit()


ch1 = Checkbutton(root2, text=1, variable=GRYaris, onvalue=1, offvalue=0, command=submit)
ch1.place(x=145, y=460)

ch2 = Checkbutton(root2, text=2, variable=GRYaris, onvalue=2, offvalue=0, command=submit)
ch2.place(x=195, y=460)

ch3 = Checkbutton(root2, text=3, variable=GRYaris, onvalue=3, offvalue=0, command=submit)
ch3.place(x=245, y=460)

ch4 = Checkbutton(root2, text=4, variable=GRYaris, onvalue=4, offvalue=0, command=submit)
ch4.place(x=295, y=460)

ch5 = Checkbutton(root2, text=5, variable=GRYaris, onvalue=5, offvalue=0, command=submit)
ch5.place(x=345, y=460)


button = tk.Button(root2, text="SUBMIT", command=submit, fg='#007acc')
button.place(x=230, y=530)
root2.mainloop()