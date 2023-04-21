from tkinter import *
from tkinter import messagebox
# import tkinter.messagebox as tmsg

root=Tk()
root.geometry("500x400")
def help():
    # tmsg.showinfo("Help", "Are you Sure you want our help")
    messagebox.showinfo("Help", "Are you Sure you want our help")
    #messagebox.showinfo-->used when you want to shows information --> only contains OK button 

def rate():
    # value=tmsg.askquestion("Experience", "Would you like to rate us?")
    value=messagebox.askquestion("Experience", "Would you like to rate us?")
    #messagebox.askquestion-->used to ask a yes/no type question --> contains Yes and No buutons
    if value=="yes":
        msg="Great! Rate us on Appstore"
    else:
        msg="Tell us what went wrong. We will Call you Soon"
    messagebox.showinfo("Rate", msg)

def download():
    # tmsg.askretrycancel("Download","Unable to download. Try again after some time")
    messagebox.askretrycancel("Download","Unable to download. Try again after some time")
    #message.askretrycancel--> used to ask a retry/cancel 


mainmenu=Menu(root)

# m1=Menu(mainmenu)
# m1.add_command(label="Home")
# m1.add_command(label="New")
# m1.add_command(label="Open")
# m1.add_separator()
# m1.add_command(label="Info")
# m1.add_command(label="Save")
# m1.add_command(label="Save As")
# m1.add_command(label="Print")
# root.config(menu=mainmenu)
# mainmenu.add_cascade(label="File", menu=m1)

m3=Menu(mainmenu,tearoff=0)
m3.add_command(label="Help", command=help)
m3.add_command(label="Rate Us", command=rate)
m3.add_command(label="Download", command=download)
mainmenu.add_cascade(label="More..", menu=m3)
root.config(menu=mainmenu)

root.mainloop()