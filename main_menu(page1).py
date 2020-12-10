
#import modules
 
from tkinter import *
import os
from PIL import ImageTk,Image 
from tkinter import font as tkFont
 
# Designing window for registration
 
def reader():
    global reader_screen
    reader_screen = Toplevel(main_screen)
    reader_screen.title("Reader")
    reader_screen.geometry("300x250")
 
    global cardnumber
    #global password
    global username_entry
    #global password_entry
    cardnumber = StringVar()
    #password = StringVar()
 
    Label(reader_screen, text="Please enter the details below").pack()
    Label(reader_screen, text="").pack()
    cardnumber_entry = Label(reader_screen, text="Card Number *")
    cardnumber_entry.pack()
    cardnumber_entry = Entry(reader_screen, textvariable=cardnumber)
    cardnumber_entry.pack()

    Label(reader_screen, text="").pack()
    Button(reader_screen, text="Submit", width=10, height=1, bg="blue").pack()
 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter the details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
# Designing Main window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("600x500")
    main_screen.title("Public Library- Main Menu")
    # Take n greater than 0.25 and less than 5
    same=True  
    n=1

    # Adding a background image
    background_image =Image.open("lib.jpg")
    [imageSizeWidth, imageSizeHeight] = background_image.size

    newImageSizeWidth = int(imageSizeWidth*n)
    if same:
        newImageSizeHeight = int(imageSizeHeight*n) 
    else:
        newImageSizeHeight = int(imageSizeHeight/n) 

    background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(background_image)

    Canvas1 = Canvas(main_screen)

    Canvas1.create_image(300,250,image = img)      
    Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(main_screen,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

    headingLabel = Label(headingFrame1, text="Welcome to \n Public Library Database", bg='black', fg='white', font=('Courier',40))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    cal28 = tkFont.Font(family='Calibri', size=28)

    btn2 = Button(main_screen,text="Adminstrator",bg='black', fg='black',font=cal28, command=login)
    btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    Label(text="").pack()
    
    btn1 = Button(main_screen,text="Reader",bg='black', fg='black',font=cal28, command=reader)
    btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
 
    main_screen.mainloop()
 
 
main_account_screen()

