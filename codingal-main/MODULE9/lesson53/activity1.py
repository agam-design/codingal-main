# Create a Tkinter Application which consists of a root window with a label and an image.
from tkinter import *
from PIL import Image, ImageTk

root=Tk()
root.title("Image Import")
root.geometry("400x400")
upload=Image.open("codingal-main/MODULE9/lesson53/cuteDog.jpg")#image.open is to open and identify the image file.
image=ImageTk.PhotoImage(upload)#convert image to the Tkinter compatible image.
label=Label(root,image=image,height=350,width=300)
label.place(x=50,y=0)
label2=Label(root,text="this is how you can image in Tkinter window")
label2.place(x=40,y=360)
root.mainloop()