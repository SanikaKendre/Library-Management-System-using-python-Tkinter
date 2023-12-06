# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 18:04:51 2023

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

username=StringVar()
Book_Id=IntVar()
Title=StringVar()
Cost=IntVar()
Quantity=IntVar()

db = sqlite3.connect('libraryproject.db')
cursor = db.cursor()
create_table ='''CREATE TABLE IF NOT EXISTS placeorder(
                            Book_Id INTEGER,
                            Title TEXT,
                            Cost INTEGER
                            
                          );'''
cursor.execute(create_table)

db.commit()

def insert():
    
  
    bid = Book_Id.get()
    ti = Title.get()
    co=Cost.get()
    db = sqlite3.connect('libraryproject.db')
    cursor = db.cursor()
    if (not isinstance(bid,int) or bid == 0):
       ms.showinfo("Message", "please enter valid Bookid")
    elif (ti.isdigit() or (ti == "")):
       ms.showinfo("Message", "please enter valid Title")
    elif (not isinstance(co,int) or co == 0):
       ms.showinfo("Message", "please enter valid Cost")
    else:
     find_user = ('SELECT * FROM signuplibrary WHERE username = ? ')
     cursor.execute(find_user,[(username.get())])
     result=cursor.fetchall()
     if result:
       
       display_query = '''SELECT Book_Id,Title,Cost FROM addbooks ;'''
       cursor.execute(display_query)
    
    
       insert_query='''INSERT INTO placeorder(Book_Id,Title,Cost) VALUES(?,?,?);'''
       user_data=(bid,ti,co)
       cursor.execute(insert_query,user_data)
       db.commit()
       db.close()
       ms.showinfo('Success!', 'Order Confirmed !')
     else:
        ms.showinfo('Error!', 'username or bookid could not be matched !')
     
    

main_label=Label(root,text="LIBRARY MANAGEMENT SYSTEM",width=43,height=1,fg="#8B3E2F",font=("times",30,"bold"))
main_label.place(x=150,y=10)

def searchbooksbutton():
    from subprocess import call
    call(['python','searchbooksuser.py'])
    
def placebooksbutton():
    from subprocess import call
    call(['python','placeorder.py'])
    
def viewbooksbutton():
    from subprocess import call
    call(['python','vieworderuser.py'])


searchbooks_button=Button(root,text="Search Books",command=searchbooksbutton,bg="#FFD39B",width=20,height=3,fg="#8B4513",font=("times",15,"bold"))
searchbooks_button.place(x=200,y=80)

placebooks_button=Button(root,text="Place Order",command=placebooksbutton,bg="#FFD39B",width=20,height=3,fg="#8B4513",font=("times",15,"bold"))
placebooks_button.place(x=550,y=80)

viewbooks_button=Button(root,text="View Order",command=viewbooksbutton,bg="#FFD39B",width=20,height=3,fg="#8B4513",font=("times",15,"bold"))
viewbooks_button.place(x=900,y=80)
frame_alpr=LabelFrame(root,width=500,height=400,font=("times",14,"bold"),bg="#CD5B45")
frame_alpr.grid(row=0,column=0)
frame_alpr.place(x=430,y=210)

sub_label=Label(root,text="PLACE ORDER",width=15,height=2,bg="#CD5B45",fg="black",font=("times",20,"bold"))
sub_label.place(x=550,y=250)

username1=Label(root,text="BookId",width=15,height=2,bg="#CD5B45",fg="black",font=("times",15,"bold"))
username1.place(x=450,y=320)

uentry=Entry(root,textvar=Book_Id,width=15,font=("times",15,"bold"))
uentry.place(x=700,y=330)

book_name=Label(root,text="Title",width=15,height=2,bg="#CD5B45",fg="black",font=("times",15,"bold"))
book_name.place(x=450,y=380)

bentry=Entry(root,textvar=Title,width=15,font=("times",15,"bold"))
bentry.place(x=700,y=390)

author_name=Label(root,text="Cost",width=15,height=2,bg="#CD5B45",fg="black",font=("times",15,"bold"))
author_name.place(x=450,y=440)

aentry=Entry(root,textvar=Cost,width=15,font=("times",15,"bold"))
aentry.place(x=700,y=450)

place_button=Button(root,command=insert,text="PLACE ORDER",bg="#FF7D40",width=12,height=1,fg="#CD2626",font=("times",15,"bold"))
place_button.place(x=600,y=530)
root.mainloop()