# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 16:01:22 2023

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
root.configure(bg="#FF7F50")

Book_Id=IntVar()
Title=StringVar()
Author_name=StringVar()
Cost=IntVar()
Quantity=IntVar()

db = sqlite3.connect('libraryproject.db')
cursor = db.cursor()
create_table ='''CREATE TABLE IF NOT EXISTS addbooks(
                            Book_Id INTEGER,
                            Title TEXT,
                            Author_name TEXT,
                            Cost INTEGER,
                            Quantity INTEGER 
                          );'''
cursor.execute(create_table)
db.commit()

def insert():
    
    bid = Book_Id.get()
    ti = Title.get()
    an=Author_name.get()
    co=Cost.get()
    qu=Quantity.get()
    
    db = sqlite3.connect('libraryproject.db')
    cursor = db.cursor()
    if (not isinstance(bid,int) or bid == 0):
       ms.showinfo("Message", "please enter valid Bookid")
    elif (ti.isdigit() or (ti == "")):
       ms.showinfo("Message", "please enter valid Title")
    elif (an.isdigit() or (an == "")):
       ms.showinfo("Message", "please enter valid Author name")
    elif (not isinstance(co,int) or co == 0):
      ms.showinfo("Message", "please enter valid Cost")
    elif (not isinstance(qu,int) or qu == 0):
       ms.showinfo("Message", "please enter valid Quantity")
    else:
       db = sqlite3.connect('libraryproject.db')
       cursor = db.cursor()
       insert_query='''INSERT INTO addbooks(Book_Id,Title,Author_name,Cost,Quantity) VALUES(?,?,?,?,?);'''
       user_data=(bid,ti,an,co,qu)
       cursor.execute(insert_query,user_data)
       db.commit()
       db.close()
       ms.showinfo('Success!', 'Book Added Successfully !')
    

main_label=Label(root,text="LIBRARY MANAGEMENT SYSTEM",width=43,height=1,fg="#8B3E2F",font=("times",30,"bold"))
main_label.place(x=150,y=10)

def addbooksbutton():
    from subprocess import call
    call(['python','addbooks.py'])
    
def searchbooksbutton():
    from subprocess import call
    call(['python','searchbooks.py'])

def updatebooksbutton():
    from subprocess import call
    call(['python','updatebooks.py'])

def vieworderbutton():
    from subprocess import call
    call(['python','vieworder.py'])

addbooks_button=Button(root,text="Add Books",command=addbooksbutton,bg="#FFD39B",width=20,height=3,fg="#8B4513",font=("times",15,"bold"))
addbooks_button.place(x=50,y=80)

searchbooks_button=Button(root,text="Search Books",command=searchbooksbutton,bg="#FFD39B",width=20,height=3,fg="#8B4513",font=("times",15,"bold"))
searchbooks_button.place(x=400,y=80)

updatebooks_button=Button(root,text="Update Books",command=updatebooksbutton,bg="#FFD39B",width=20,height=3,fg="#8B4513",font=("times",15,"bold"))
updatebooks_button.place(x=750,y=80)

viewbooks_button=Button(root,text="View Order",command=vieworderbutton,bg="#FFD39B",width=20,height=3,fg="#8B4513",font=("times",15,"bold"))
viewbooks_button.place(x=1100,y=80)

frame_alpr=LabelFrame(root,width=645,height=480,font=("times",14,"bold"),bg="#CD5B45")
frame_alpr.grid(row=0,column=0)
frame_alpr.place(x=350,y=210)

sub_label=Label(root,text="ADD BOOKS",width=15,height=2,bg="#CD5B45",fg="black",font=("times",20,"bold"))
sub_label.place(x=550,y=220)

book_id=Label(root,text="Book Id",width=15,height=2,bg="#CD5B45",fg="black",font=("times",15,"bold"))
book_id.place(x=450,y=300)

bentry=Entry(root,textvar=Book_Id,width=15,font=("times",15,"bold"))
bentry.place(x=700,y=310)

title=Label(root,text="Title",width=15,height=2,bg="#CD5B45",fg="black",font=("times",15,"bold"))
title.place(x=450,y=350)

tentry=Entry(root,textvar=Title,width=15,font=("times",15,"bold"))
tentry.place(x=700,y=360)

author_name=Label(root,text="Author Name",width=15,height=2,bg="#CD5B45",fg="black",font=("times",15,"bold"))
author_name.place(x=450,y=400)

aentry=Entry(root,textvar=Author_name,width=15,font=("times",15,"bold"))
aentry.place(x=700,y=410)

cost=Label(root,text="Cost",width=15,height=2,bg="#CD5B45",fg="black",font=("times",15,"bold"))
cost.place(x=450,y=450)

centry=Entry(root,textvar=Cost,width=15,font=("times",15,"bold"))
centry.place(x=700,y=460)

quantity=Label(root,text="Quantity",width=15,height=2,bg="#CD5B45",fg="black",font=("times",15,"bold"))
quantity.place(x=450,y=500)

qentry=Entry(root,textvar=Quantity,width=15,font=("times",15,"bold"))
qentry.place(x=700,y=510)

add_button=Button(root,command=insert,text="ADD",bg="#FF7D40",width=10,height=1,fg="#CD2626",font=("times",15,"bold"))
add_button.place(x=600,y=600)
root.mainloop()