# Create a root window that contains a button. And when the user clicks this button, then a new window will open up using the Top Level functionality of Tkinter.
from tkinter import*
root=Tk()
root.geometry("400x300")
root.title("main")

def topWindowClick():
    top=Toplevel()
    top.geometry("180x100")
    top.title("top")
    label2=Label(top,text="this the top level window")
    label2.pack()

label=Label(root,text="this the root window")
btn=Button(root,text="click here to opeen another window.",command=topWindowClick)
label.pack()
btn.pack()
root.mainloop()

