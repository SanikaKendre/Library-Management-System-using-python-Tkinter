# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 16:01:22 2023

@author: DELL
"""

from tkinter import *
from PIL import Image,ImageTk
root= Tk()
root.title("Welcome to Library Management application")
root.geometry('450x300')


image1=Image.open("libraryinfo.jpg")
image1=image1.resize((1800,700),Image.ANTIALIAS)
background_image=ImageTk.PhotoImage(image1)
background_label=Label(root,image=background_image)
background_label.image=background_image
background_label.place(x=0,y=40)


main_label=Label(root,text="LIBRARY MANAGEMENT SYSTEM",width=90,height=1,bg="#E9967A",fg="#8B3E2F",font=("times",20,"bold"))
main_label.place(x=0,y=5)

def addbooks_button():
    from subprocess import call
    call(['python','addbooks.py'])
def searchbooks_button():
    from subprocess import call
    call(['python','searchbooks.py'])
def updatebooks_button():
    from subprocess import call
    call(['python','updatebooks.py'])
def viewbooks_button():
    from subprocess import call
    call(['python','vieworder.py'])

addbooks_button=Button(root,text="Add Books",command=addbooks_button,bg="#FFD39B",width=20,height=10,fg="#8B4513",font=("times",15,"bold"))
addbooks_button.place(x=50,y=250)

searchbooks_button=Button(root,text="Search Books",command=searchbooks_button,bg="#FFD39B",width=20,height=10,fg="#8B4513",font=("times",15,"bold"))
searchbooks_button.place(x=400,y=250)

updatebooks_button=Button(root,text="Update Books",command=updatebooks_button,bg="#FFD39B",width=20,height=10,fg="#8B4513",font=("times",15,"bold"))
updatebooks_button.place(x=750,y=250)

viewbooks_button=Button(root,text="View Order",command=viewbooks_button,bg="#FFD39B",width=20,height=10,fg="#8B4513",font=("times",15,"bold"))
viewbooks_button.place(x=1100,y=250)
root.mainloop()