
from tkinter import *
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
root= Tk()
root.title("Welcome to Library Management application")
root.geometry('700x900')
image1=Image.open("librarysignup.png")
image1=image1.resize((700,550),Image.ANTIALIAS)
background_image=ImageTk.PhotoImage(image1)
background_label=Label(root,image=background_image)
background_label.image=background_image
background_label.place(x=650,y=130)

fullname=StringVar()
age=IntVar()
mobilenumber=IntVar()
Email=StringVar()
username=StringVar()
password=StringVar()

db = sqlite3.connect('libraryproject.db')
cursor = db.cursor()
create_table ='''CREATE TABLE IF NOT EXISTS signuplibrary(
                            fullname TEXT,
                            age INTEGER,
                            mobilenumber INTEGER,
                            Email TEXT,
                            username TEXT,
                            password TEXT
                          );'''
cursor.execute(create_table)
db.commit()
def password_check(passwd): 
	
	SpecialSym =['$', '@', '#', '%'] 
	val = True
	
	if len(passwd) < 6: 
		print('length should be at least 6') 
		val = False
		
	if len(passwd) > 20: 
		print('length should be not be greater than 8') 
		val = False
		
	if not any(char.isdigit() for char in passwd): 
		print('Password should have at least one numeral') 
		val = False
		
	if not any(char.isupper() for char in passwd): 
		print('Password should have at least one uppercase letter') 
		val = False
		
	if not any(char.islower() for char in passwd): 
		print('Password should have at least one lowercase letter') 
		val = False
		
	if not any(char in SpecialSym for char in passwd): 
		print('Password should have at least one of the symbols $@#') 
		val = False
        
	if val: 
		return val 


def insert():
    fname = fullname.get()
    ag = age.get()
    mob = mobilenumber.get()
    email1=Email.get()
    user = username.get()
    pas = password.get()
    
    db = sqlite3.connect('libraryproject.db')
    cursor = db.cursor()
    find_user = ('SELECT * FROM signuplibrary WHERE username = ?')
    cursor.execute(find_user, [(username.get())])

   # else:
   #   ms.showinfo('Success!', 'Account Created Successfully !')

   # to check mail
   #regex = '^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$'
    regex='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex, email1)):
       a = True
    else:
       a = False
   # validation
    if (fname.isdigit() or (fname == "")):
       ms.showinfo("Message", "please enter valid name")
    
    elif (email1 == "") or (a == False):
       ms.showinfo("Message", "Please Enter valid email")
    elif((len(str(mob)))<10 or len(str((mob)))>10):
       ms.showinfo("Message", "Please Enter 10 digit mobile number")
    elif ((ag> 100) or (ag == 0)):
       ms.showinfo("Message", "Please Enter valid age")
    elif (cursor.fetchall()):
       ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
    elif (pas == ""):
       ms.showinfo("Message", "Please Enter valid password")
    
       
    elif(pas=="")or(password_check(pas))!=True:
       ms.showinfo("Message", "password must contain atleast 1 Uppercase letter,1 symbol,1 number")
    
    else:
       db = sqlite3.connect('libraryproject.db')
       cursor = db.cursor()
       
       insert_query='''INSERT INTO signuplibrary(fullname,age,mobilenumber,Email,username,password) VALUES(?,?,?,?,?,?);'''
       user_data=(fname,ag,mob,email1,user,pas)
       cursor.execute(insert_query,user_data)
       db.commit()
       db.close()
       ms.showinfo('Success!', 'Account Created Successfully !')
       from subprocess import call
       call(['python','librarysignin.py'])
    
    
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

frame_alpr=LabelFrame(root,width=645,height=550,font=("times",14,"bold"),bg="#CD5B45")
frame_alpr.grid(row=0,column=0)
frame_alpr.place(x=10,y=130)

label=Label(root,text="SIGN UP",bg="#EE7621",width=30,height=1,fg="white",font=("times",20,"bold"))
label.place(x=100,y=150)

name=Label(root,text="Name",bg="#FF9912",width=15,height=1,fg="white",font=("times",15,"bold"))
name.place(x=100,y=250)

nentry=Entry(root,textvar=fullname,width=15,font=("times",15,"bold"))
nentry.place(x=400,y=250)

age1=Label(root,text="Age",bg="#FF9912",width=15,height=1,fg="white",font=("times",15,"bold"))
age1.place(x=100,y=300)

aentry=Entry(root,textvar=age,width=15,font=("times",15,"bold"))
aentry.place(x=400,y=300)

mobileno=Label(root,text="Mobile Number",bg="#FF9912",width=15,height=1,fg="white",font=("times",15,"bold"))
mobileno.place(x=100,y=350)

mentry=Entry(root,textvar=mobilenumber,width=15,font=("times",15,"bold"))
mentry.place(x=400,y=350)

email=Label(root,text="Email",bg="#FF9912",width=15,height=1,fg="white",font=("times",15,"bold"))
email.place(x=100,y=400)

eentry=Entry(root,textvar=Email,width=15,font=("times",15,"bold"))
eentry.place(x=400,y=400)

username1=Label(root,text="Username",bg="#FF9912",width=15,height=1,fg="white",font=("times",15,"bold"))
username1.place(x=100,y=450)

uentry=Entry(root,textvar=username,width=15,font=("times",15,"bold"))
uentry.place(x=400,y=450)

password1=Label(root,text="Password",bg="#FF9912",width=15,height=1,fg="white",font=("times",15,"bold"))
password1.place(x=100,y=500)

pentry=Entry(root,textvar=password,width=15,font=("times",15,"bold"))
pentry.place(x=400,y=500)


    

button=Button(root,text="Submit",bg="#ED9121",width=15,height=2,fg="white",font=("times",15,"bold"),command=insert)
button.place(x=250,y=600)


root.mainloop()
