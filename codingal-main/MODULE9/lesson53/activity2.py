# Create a Tkinter Application which consists of a root window with a button (with text Scan for the virus). When this button is clicked, it will generate a message box that shows a warning that - Stop! Virus Found.
from tkinter import*
from tkinter import messagebox

root=Tk()
root.geometry("200x200")
def message():
    messagebox.showwarning("alert!","stop virus found.")#message box widget used here is showWarning.

btn=Button(root,text="scan for virus.",command=message)
btn.place(x=40,y=80)
root.mainloop()

