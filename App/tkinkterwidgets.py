import tkinter as tk
from tkinter import *

def dropdown(formwindow):
    OptionList = [
        "Monitor",
        "Tower",
    ]

    vdropdown = tk.StringVar(formwindow)
    vdropdown.set(OptionList[0])

    return tk.OptionMenu(formwindow, vdropdown, *OptionList)


def checkbox(formwindow):
    return Checkbutton(formwindow, text="")


def easset(formwindow):
    return Entry(formwindow, text="scan asset")


def bdone(formwindow):
    return Button(formwindow, text="press here when done")


def bclear(formwindow):
    return Button(formwindow, text="clear")
