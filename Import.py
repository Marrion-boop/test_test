from tkinter import *

root = Tk()

root.geometry('1280x720')

Username = Entry(root,width=23)
Password = Entry(root,width=23, show = "*")
UsernameSign = Entry(root, width=23)
PasswordSign = Entry(root,width=23, show = "*")

def login(event=NONE):
    UserText = Label(root, text="Username:")
    UserText.grid(row=3, column=1)    
    Username.grid(row=3,column=2)
    root.bind('<Return>',loginPass)

def loginPass(event=NONE):
    PassText = Label(root, text="Password:")
    PassText.grid(row=4, column=1)
    Password.focus()
    Password.grid(row=4,column=2)

def signup(event=NONE):
    UserSignText = Label(root, text="Type Desired Username:")
    UserSignText.grid(row=3, column=1)
    UsernameSign.grid(row=3,column=2)
    root.bind('<Return>',signupPass)

def signupPass(event=NONE):
    PassSignText = Label(root, text="Type Desired Password:")
    PassSignText.grid(row=4, column=1)
    PasswordSign.focus()
    PasswordSign.grid(row=4,column=2)

Username.bind('<Return>', login)

ProjText = Label(root, text="A Drey and Marrion Project")
Budget = Label(root, text="Budget Tracker")
signup = Button(root, text="Sign up", padx=40, command=signup)
login = Button(root, text="Login", padx=40, command=login, bg="light green")
importAcc = Button(root, text="Import Account", padx=10)



signup.grid(row=2, column=1)
login.grid(row=2, column=2)
importAcc.grid(row=2, column=3)
ProjText.grid(row=0, column=2)
Budget.grid(row=1, column=2)


root.mainloop()

print("Hello World")
print("Hello World - drey")