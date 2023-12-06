# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 11:28:13 2023

@author: DELL
"""


from tkinter import *
from PIL import Image,ImageTk
root= Tk()
root.title("Welcome to Library Management application")
root.geometry('450x300')
image1=Image.open("library.png")
image1=image1.resize((1800,550),Image.ANTIALIAS)
background_image=ImageTk.PhotoImage(image1)
background_label=Label(root,image=background_image)
background_label.image=background_image
background_label.place(x=0,y=130)

main_label=Label(root,text="LIBRARY MANAGEMENT SYSTEM",width=43,height=1,fg="#8B3E2F",font=("times",30,"bold"))
main_label.place(x=150,y=0)

sub_label=Label(root,bg="grey",width=90,height=2,fg="white",font=("times",20,"bold"))
sub_label.place(x=0,y=50)


def homebutton():
    from subprocess import call
    call(['python','libraryhomepage.py'])
def aboutbutton():
    from subprocess import call
    call(['python','libraryaboutuspage.py'])
def contactbutton():
    from subprocess import call
    call(['python','contactuslibrary.py'])
def signupbutton():
    from subprocess import call
    call(['python','librarysignup.py'])

def signinbutton():
    from subprocess import call
    call(['python','librarysignin.py'])

def adminbutton():
    from subprocess import call
    call(['python','adminsignin.py'])
    
def userbutton():
    from subprocess import call
    call(['python','librarysignup.py'])
    
home_button=Button(root,text="Home",command=homebutton,bg="#FFD39B",width=10,height=1,fg="#8B4513",font=("times",15,"bold"))
home_button.place(x=150,y=65)

signup_button=Button(root,text="Sign Up",command=signupbutton,bg="#FFD39B",width=10,height=1,fg="#8B4513",font=("times",15,"bold"))
signup_button.place(x=350,y=65)

signin_button=Button(root,text="Sign In",command=signinbutton,bg="#FFD39B",width=10,height=1,fg="#8B4513",font=("times",15,"bold"))
signin_button.place(x=550,y=65)

about_button=Button(root,text="About Us",command=aboutbutton,bg="#FFD39B",width=10,height=1,fg="#8B4513",font=("times",15,"bold"))
about_button.place(x=750,y=65)

contact_button=Button(root,text="Contact Us",command=contactbutton,bg="#FFD39B",width=10,height=1,fg="#8B4513",font=("times",15,"bold"))
contact_button.place(x=950,y=65)

admin_button=Button(root,text="ADMIN",command=adminbutton,bg="#FF7F50",width=25,height=15,fg="white",font=("times",15,"bold"))
admin_button.place(x=150,y=250)

user_button=Button(root,text="USER",command=userbutton,bg="#FF7F50",width=25,height=15,fg="white",font=("times",15,"bold"))
user_button.place(x=850,y=250)


root.mainloop()