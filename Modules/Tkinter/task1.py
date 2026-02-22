# Login form
import tkinter as tk
from tkinter import messagebox # it is a popup just like alert in js
root=tk.Tk() # main window object is created
name=tk.Label(root,text="Name :").grid(row=0,column=0)
password=tk.Label(root,text="Password :").grid(row=1,column=0)
Inputname=tk.Entry(root)
Inputname.grid(row=0,column=1)
Inputpassword=tk.Entry(root,show="*")
Inputpassword.grid(row=1,column=1)

def check():
    myname="tharun"
    mypassword="Tharunkumar"
    if Inputname.get()==myname and Inputpassword.get()==mypassword:
        messagebox.showinfo(title="correct",message="Sucessfully login!")
    else:
        messagebox.showwarning(title="Oops!",message="Password/username wrong entered,Try again!")

btn=tk.Button(root,text="Login",command=check).grid(row=2,column=1)

root.mainloop()
