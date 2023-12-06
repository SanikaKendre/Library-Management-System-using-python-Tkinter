# -- coding: utf-8 --
"""
Created on Wed Nov  8 08:52:52 2023

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
image1=Image.open("librarysignin.jpg")
image1=image1.resize((700,550),Image.ANTIALIAS)
background_image=ImageTk.PhotoImage(image1)
background_label=Label(root,image=background_image)
background_label.image=background_image
background_label.place(x=650,y=130)

username=StringVar()
password=StringVar()


db = sqlite3.connect('libraryproject.db')
cursor = db.cursor()
create_table ='''CREATE TABLE IF NOT EXISTS signinlibrary(
                            username TEXT,
                            password TEXT
                          );'''
cursor.execute(create_table)


db.commit()
db.close()




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
        call(['python','libraryinfouser.py'])
    else:
        ms.showinfo("oops!","username or password are not found match")
    
     
    

main_label=Label(root,text="LIBRARY MANAGEMENT SYSTEM",width=43,height=1,fg="#8B3E2F",font=("times",30,"bold"))
main_label.place(x=150,y=0)

sub_label=Label(root,bg="grey",width=90,height=2,fg="white",font=("times",20,"bold"))
sub_label.place(x=0,y=50)

home_button=Button(root,text="Home",bg="#FFD39B",width=10,height=1,fg="#8B4513",font=("times",15,"bold"))
home_button.place(x=150,y=65)

signup_button=Button(root,text="Sign Up",bg="#FFD39B",width=10,height=1,fg="#8B4513",font=("times",15,"bold"))
signup_button.place(x=350,y=65)

signin_button=Button(root,text="Sign In",bg="#FFD39B",width=10,height=1,fg="#8B4513",font=("times",15,"bold"))
signin_button.place(x=550,y=65)

about_button=Button(root,text="About Us",bg="#FFD39B",width=10,height=1,fg="#8B4513",font=("times",15,"bold"))
about_button.place(x=750,y=65)

contact_button=Button(root,text="Contact Us",bg="#FFD39B",width=10,height=1,fg="#8B4513",font=("times",15,"bold"))
contact_button.place(x=950,y=65)

frame_alpr=LabelFrame(root,width=645,height=550,font=("times",14,"bold"),bg="#CDAA7D")
frame_alpr.grid(row=0,column=0)
frame_alpr.place(x=10,y=130)

label=Label(root,text="SIGN IN",bg="#8B7355",width=30,height=1,fg="white",font=("times",20,"bold"))
label.place(x=100,y=150)

username1=Label(root,text="Username",bg="#FF9912",width=15,height=1,fg="white",font=("times",15,"bold"))
username1.place(x=100,y=250)

uentry=Entry(root,textvar=username,width=15,font=("times",15,"bold"))
uentry.place(x=400,y=250)

password1=Label(root,text="Password",bg="#FF9912",width=15,height=1,fg="white",font=("times",15,"bold"))
password1.place(x=100,y=350)

pentry=Entry(root,textvar=password,width=15,font=("times",15,"bold"))
pentry.place(x=400,y=350)

button=Button(root,text="Signin",command=insert,bg="#FF7F50",width=15,height=2,fg="white",font=("times",15,"bold"))
button.place(x=230,y=450)

forget_username=Label(root,text="Forget Username?",bg="white",width=14,height=1,fg="#0000CD",font=("times",10,"bold"))
forget_username.place(x=230,y=515)

forget_password=Label(root,text="Forget Password ?",bg="white",width=14,height=1,fg="#0000CD",font=("times",10,"bold"))
forget_password.place(x=230,y=530)

root.mainloop()