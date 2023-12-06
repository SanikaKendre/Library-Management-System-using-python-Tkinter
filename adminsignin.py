# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 18:44:55 2023

@author: DELL
"""

from tkinter import *
from PIL import Image,ImageTk
import sqlite3
from tkinter import messagebox as ms
import re

root= Tk()
root.title("Welcome to Library Management application")
root.geometry('700x900')
main_label=Label(root,text="LIBRARY MANAGEMENT SYSTEM",bg="#FFF68F",width=43,height=1,fg="#8B3E2F",font=("times",30,"bold"))
main_label.place(x=200,y=0)
root.configure(bg="#FFF68F")

username=StringVar()
password=StringVar()


def insert():
    
    user = username.get()
    pas = password.get()
    if not user.strip or not pas.strip():
       ms.showinfo("Error!","username and password cannot be blank") 
       return
    db = sqlite3.connect('libraryproject.db')
    cursor = db.cursor()
    find_user = ('SELECT * FROM signuplibrary WHERE username = ? AND password=?')
    cursor.execute(find_user,[(username.get()),(password.get())])
    result=cursor.fetchall()
    if result:
       msg=""
       print(msg)
       ms.showinfo("message","login successfully")
       from subprocess import call
       call(['python','libraryinfo.py'])
    else:
       ms.showinfo("oops!","username or password are not found match")
    
    

frame_alpr=LabelFrame(root,width=550,height=450,font=("times",14,"bold"),bg="#EEE685")
frame_alpr.grid(row=0,column=0)
frame_alpr.place(x=450,y=130)

username1=Label(root,text="Username",bg="#EEE685",width=15,height=1,fg="black",font=("times",15,"bold"))
username1.place(x=500,y=250)

uentry=Entry(root,textvar=username,width=15,font=("times",15,"bold"))
uentry.place(x=750,y=250)

password1=Label(root,text="Password",bg="#EEE685",width=15,height=1,fg="black",font=("times",15,"bold"))
password1.place(x=500,y=350)

pentry=Entry(root,textvar=password,width=15,font=("times",15,"bold"))
pentry.place(x=750,y=350)



button=Button(root,text="Signin",command=insert,width=15,height=1,fg="black",font=("times",15,"bold"))
button.place(x=650,y=450)
root.mainloop()