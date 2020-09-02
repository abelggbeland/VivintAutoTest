import base64
import os
from tkinter import *
import tkinkterform
import Sender

def main():
    if not os.path.exists("Credentials"):
        open("Credentials", "w+")
        loginwindow()
    else:
        tkinkterform.jirawindow()

def loginwindow():
    def validateLogin():
        invalidLogin = Label(tkWindow, text="Invalid login")
        invalidLogin.grid_forget()
        f = open("Credentials", "w+")
        f.write(base64.b64encode(str(usernameEntry.get()).encode()).decode() + "\n")
        f.write(base64.b64encode(str(passwordEntry.get()).encode()).decode())
        f.close()

        if not Sender.auth().status_code == 200:
            os.remove("Credentials")
            passwordEntry.delete('0', END)
            usernameEntry.delete('0', END)
            invalidLogin.grid(row=5, column=2)
        else:
            tkWindow.destroy()
            tkinkterform.jirawindow()

    # window
    tkWindow = Tk()
    tkWindow.title("Log in")

    # username label and text entry box
    usernameLabel = Label(tkWindow, text="Email")
    email = StringVar()
    usernameEntry = Entry(tkWindow, textvariable=email)

    # password label and password entry box
    passwordLabel = Label(tkWindow, text="API Token")
    APIKey = StringVar()
    passwordEntry = Entry(tkWindow, textvariable=APIKey, show='*')

    # login button
    loginButton = Button(tkWindow, text="Login", command=validateLogin)

    ####place widgets
    usernameLabel.grid(row=0, column=0)
    usernameEntry.grid(row=0, column=2)
    passwordLabel.grid(row=1, column=0)
    passwordEntry.grid(row=1, column=2)
    loginButton.grid(row=100, column=1)

    tkWindow.mainloop()

main()
