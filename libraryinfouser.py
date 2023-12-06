# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 19:39:21 2023

@author: DELL
"""
from tkinter import *
from PIL import Image,ImageTk
root= Tk()
root.title("Welcome to Library Management application")
root.geometry('450x300')


image1=Image.open("libraryinfouser.jpeg")
image1=image1.resize((1800,700),Image.ANTIALIAS)
background_image=ImageTk.PhotoImage(image1)
background_label=Label(root,image=background_image)
background_label.image=background_image
background_label.place(x=0,y=40)


main_label=Label(root,text="LIBRARY MANAGEMENT SYSTEM",width=90,height=1,bg="#E9967A",fg="#8B3E2F",font=("times",20,"bold"))
main_label.place(x=0,y=5)

def searchbooksuser_button():
    from subprocess import call
    call(['python','searchbooksuser.py'])
def placeorder_button():
    from subprocess import call
    call(['python','placeorder.py'])
def vieworder_button():
    from subprocess import call
    call(['python','vieworderuser.py'])


searchbooks_button=Button(root,text="Search Books",command=searchbooksuser_button,bg="#FFD39B",width=20,height=10,fg="#8B4513",font=("times",15,"bold"))
searchbooks_button.place(x=50,y=250)

updatebooks_button=Button(root,text="Place Order",command=placeorder_button,bg="#FFD39B",width=20,height=10,fg="#8B4513",font=("times",15,"bold"))
updatebooks_button.place(x=550,y=250)

viewbooks_button=Button(root,text="View Order",command=vieworder_button,bg="#FFD39B",width=20,height=10,fg="#8B4513",font=("times",15,"bold"))
viewbooks_button.place(x=1050,y=250)
root.mainloop()