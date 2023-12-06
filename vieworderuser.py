# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 18:46:11 2023

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
Cost=IntVar()




def insert():
    
    bid = Book_Id.get()
    ti = Title.get()
    co=Cost.get()
   
    
    
    db = sqlite3.connect('libraryproject.db')
    cursor = db.cursor()
    find_user = ('SELECT Book_Id,Title,Cost FROM placeorder WHERE Book_Id=?;')
    cursor.execute(find_user, [int(bid)])
    result = cursor.fetchall()
    if (not isinstance(bid,int) or bid == 0):
       ms.showinfo("Message", "please enter valid Bookid")
    elif result:
        display_query = '''SELECT Book_Id,Title,Author_name,Cost,Quantity FROM addbooks WHERE Book_Id=?;'''
        cursor.execute(display_query, [int(bid)])
        result = cursor.fetchone()
        db.commit()
        ms.showinfo("success data fetched succesfully")
    else:
        ms.showinfo("error record not found for book id")

    insert_query='''INSERT INTO vieworderuser(Bookid) VALUES(?);'''
    user_data=(bid,)
    cursor.execute(insert_query,user_data)
    db.commit()
    db.close()
    
    
    


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

sub_label=Label(root,text="VIEW ORDER",width=15,height=2,bg="#CD5B45",fg="black",font=("times",20,"bold"))
sub_label.place(x=550,y=250)

book_id=Label(root,text="Book Id",width=15,height=2,bg="#CD5B45",fg="black",font=("times",15,"bold"))
book_id.place(x=450,y=350)

bentry=Entry(root,textvar=Book_Id,width=15,font=("times",15,"bold"))
bentry.place(x=700,y=360)

view_button=Button(root,command=insert,text="VIEW ORDER",bg="#FF7D40",width=12,height=1,fg="#CD2626",font=("times",15,"bold"))
view_button.place(x=600,y=450)

root.mainloop()