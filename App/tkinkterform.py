from tkinter import *

import APICalls
import tkinkterwidgets
import Data
import Sender


def canImport(labelName, lableBadgeId, dropdowns):
    canBool = True
    if not labelName and labelName.strip():
        canBool = False

    if not lableBadgeId and lableBadgeId.strip():
        canBool = False

    return canBool


def jirawindow():
    def clear():
        pass

    def exportData():
        if canImport(str(labelNameEntry.get()),
                     str(lableBadgeIdEntry.get()),
                     dropdowns):
            data = Data.data(str(labelNameEntry.get()), str(lableBadgeIdEntry.get()), dropdowns, checkboxs)
            Sender.send(APICalls.makeIssue(data), "https://vivint.atlassian.net/rest/api/3/issue")
        else:
            clear()

    formwindow = Tk()
    formwindow.title("Returns")  # to define the title
    dropdowns = []
    checkboxs = []

    buttonDone = Button(formwindow, text="press here when done", command=exportData)
    buttonclear = Button(formwindow, text="clear", command=clear)

    labelName = Label(formwindow, text="Please provide your name. ")
    labelNameEntry = Entry(formwindow, text="name")
    labelNameEntry.grid(row=0, column=2)

    lableBadgeId = Label(formwindow, text="Please provide your badge id. ")
    lableBadgeIdEntry = Entry(formwindow, text="line")
    lableBadgeIdEntry.grid(row=1, column=2)

    lableKeyboard = Label(formwindow, text="Did you return a keboard? ")
    labelMouse = Label(formwindow, text="Did you return a mouse? ")
    labelHeadset = Label(formwindow, text="Did you return a headset? ")

    for i in range(2):
        dropdown = tkinkterwidgets.dropdown(formwindow)
        entry = Entry(formwindow, text="line" + str(i))
        dropdown.grid(row=2 + i, column=0)
        entry.grid(row=2 + i, column=2)
        dropdowns.append([dropdown, entry])

    for i in range(3):
        var = IntVar()
        checkbox = Checkbutton(formwindow, text="", variable=var)
        checkbox.grid(row=13, column=0 + i)
        checkboxs.append(var)

    labelName.grid(row=0, column=0)
    lableBadgeId.grid(row=1, column=0)

    lableKeyboard.grid(row=12, column=0)
    labelMouse.grid(row=12, column=1)
    labelHeadset.grid(row=12, column=2)

    buttonDone.grid(row=99, column=1)
    buttonclear.grid(row=99, column=2)

    formwindow.mainloop()

