import tkinter as tk
from tkinter import *

class FEEDBACK:
    def __init__(self):
        self.root = Tk()
        self.root.title = "FEEDBACK"
        self.root.geometry("910x580")
        self.btn = tk.Button(self.root, text="FEEDBACK", font=("Arial", 13), command=self.namesx)
        self.btn.pack(pady=200)
        self.root.mainloop()
    def namesx(self):
        self.root2 = Tk()
        self.root2.title = "FEEDBACK"
        self.root2.geometry("910x580")
        self.fback=tk.Label(self.root2, text="Hi!!! If you have any questions or concerns about this app, \n "
                              "please contact us through our Gmail accounts.", font=("Arial", 13))
        self.fback.pack(pady=80)

        self.fback1=tk.Label(self.root2, text="abdullahadel.rante@evsu.edu.ph \n "
                                 "johnpaul.vasquez@evsu.edu.phn\n"
                                 "nathandhale.marabiles10@evsu.edu.ph", font=("Arial",15),)
        self.fback1.pack(pady=5)

        self.fback2 = tk.Label(self.root2, text="Thank you!!! <3", font=("Arial", 13), fg="red")
        self.fback2.pack(pady=20)
        self.root2.mainloop()
FEEDBACK()

