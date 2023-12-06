# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 16:05:42 2023

@author: DELL
"""

from tkinter import *
from PIL import Image,ImageTk
root= Tk()
root.title("Welcome to Library Management application")
root.geometry('450x300')
image1=Image.open("aboutuslibrary.jpg")
image1=image1.resize((1350,550),Image.ANTIALIAS)
background_image=ImageTk.PhotoImage(image1)
background_label=Label(root,image=background_image)
background_label.image=background_image
background_label.place(x=0,y=130)

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

main_text_label=Label(root,text="ABOUT US",bg="#F0E68C",fg="black",font=("times",30,"bold"))
main_text_label.place(x=600,y=150)

text_label=Label(root,text="Hello !!! Welcome to Library Management System",bg="#EECFA1",fg="black",font=("times",15,"bold"))
text_label.place(x=500,y=250)

sub_text_label=Label(root,text="This web application is used to help people access books available in library .\n It provides a user friendly interface application to the users where he can do all the operations of regarding books very easily.\n To create an automataed and computerized version for a library so that the daily work of a library can be managed and monitored easily and efficiently.\n If you want to create account please go to the sign up option and fill the information all and submit it.",bg="#8B814C",fg="black",font=("times",15,"bold"))
sub_text_label.place(x=30,y=300)
root.mainloop()
