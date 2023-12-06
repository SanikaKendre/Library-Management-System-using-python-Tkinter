# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 17:28:37 2023

@author: DELL
"""
from tkinter import *
from PIL import Image,ImageTk
import sqlite3
from tkinter import messagebox as ms
import re

root= Tk()
root.title("Welcome to Library Management application")
root.geometry('450x300')
image1=Image.open("contactuslibrary.jpg")
image1=image1.resize((1350,550),Image.ANTIALIAS)
background_image=ImageTk.PhotoImage(image1)
background_label=Label(root,image=background_image)
background_label.image=background_image
background_label.place(x=0,y=130)

fullname=StringVar()
Email=StringVar()
Reason=StringVar()
db = sqlite3.connect('libraryproject.db')
cursor = db.cursor()
create_table ='''CREATE TABLE IF NOT EXISTS contactus(
                            fullname TEXT,
                            Email TEXT,
                            Reason TEXT
                          );'''

cursor.execute(create_table)
db.commit()

def insert():
    
    nm = fullname.get()
    em = Email.get()
    re=messageentry.get("1.0","end-1c")
    if not nm.strip() or not em.strip() or not re.strip():
       ms.showinfo("Error!","name,email and reason cannot be blank") 
       return
    db = sqlite3.connect('libraryproject.db')
    cursor = db.cursor()
    find_user=('SELECT * FROM signuplibrary WHERE fullname=? AND Email=?')
    cursor.execute(find_user,[(fullname.get()),(Email.get())])
    result=cursor.fetchall()
    if not result:
       ms.showinfo("Error!","name and email could not be matched") 
       return
    else:
     insert_query='''INSERT INTO contactus(fullname,Email,Reason) VALUES(?,?,?);'''
     user_data=(nm,em,re)
     cursor.execute(insert_query,user_data)
     db.commit()
     db.close()
     ms.showinfo("Success","Reason submitted successfully") 

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

frame_alpr=LabelFrame(root,width=500,height=400,bd=5,font=("times",14,"bold"),bg="#8B4500")
frame_alpr.grid(row=0,column=0,sticky="nw")
frame_alpr.place(x=400,y=200)

fname=Label(root,text="Name",bg="#CD6600",width=15,height=1,fg="white",font=("times",15,"bold"))
fname.place(x=450,y=250)

fentry=Entry(root,textvar=fullname,width=15,font=("times",15,"bold"))
fentry.place(x=700,y=250)

email=Label(root,text="Email",bg="#CD6600",width=15,height=1,fg="white",font=("times",15,"bold"))
email.place(x=450,y=300)

eentry=Entry(root,textvar=Email,width=15,font=("times",15,"bold"))
eentry.place(x=700,y=300)

messagebox=Label(root,text="Reason",bg="#CD6600",width=15,height=1,fg="white",font=("times",15,"bold"))
messagebox.place(x=450,y=350)

messageentry=Text(root,height=4,width=20)
messageentry.place(x=700,y=350)

button=Button(root,command=insert,text="Submit Reason",bg="#8B4513",width=15,height=1,fg="white",font=("times",15,"bold"))
button.place(x=550,y=450)

root.mainloop()