import os 
import subprocess
from tkinter import *
from cloudbian_lite import fontlib
from tkinter import messagebox

root = Tk()
root.title("Bootfile Setup")
root.resizable(True, True)

def label(text, font=fontlib.default):
    Label(root, text=text, font=font).pack(side="left", anchor="nw")

def button(text, command, font=fontlib.default):
    Button(root, text=text, command=command, font=font).pack(side="left", anchor="nw")
    
label("Click this button to check if the bootfile exists")

def check_file():
    exist:bool = os.path.exists("~/.cloudfile")
    if exist == True:
        messagebox.showinfo(parent=root, title="System BIOS", message="~/.cloudbian Folder exists")


root.mainloop()