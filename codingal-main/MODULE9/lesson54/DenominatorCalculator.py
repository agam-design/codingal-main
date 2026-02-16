# Write a Python program to create a Denominator Calculator to calculate the number of notes of denominations - 2000, 500, and 100 for the amount entered by the user. and create its GUI for the user by using the Tkinter library.
from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk

root=Tk()
root.title("Denomination Calculator")
root.configure(bg="light blue")
root.geometry("650x400")

upload=Image.open("codingal-main/MODULE9/lesson54/denomination.png")
upload=upload.resize((300,300))
image=ImageTk.PhotoImage(upload)
label=Label(root,image=image,bg="light blue")
label.place(x=180,y=20)
label1=Label(root,text="welcome to denomination calculation app.")
label1.place(relx=.5,y=340,anchor=CENTER)

def msg():#function defination
    msgBox=messagebox.showinfo("ALERT!","Do you want to calculate the denomination count.")
    if msgBox=="ok":
        topwin()

btn1=Button(root,text="click here",bg="brown",fg="white",command=msg)#function call
btn1.place(x=260,y=360)

def topwin():
    top=Toplevel()
    top.title("Denomination Calculator")
    top.configure(bg="light grey")
    top.geometry("600x350+50+50")
    label=Label(top,text="ENTER TOTAL AMOUNT.",bg="light grey")
    entry1=Entry(top)
    lb=Label(top,text="Here are the total number of notes for each denomination",bg="light grey")
    lb1=Label(top,text="2000",bg="light grey")
    lb2=Label(top,text="500",bg="light grey")
    lb3=Label(top,text="100",bg="light grey")
    t1=Entry(top)
    t2=Entry(top)
    t3=Entry(top)

    def calculator():
        try:
            global amount 
            amount=int(entry1.get())
            note2000=amount//2000
            amount%=2000
            note500=amount//500
            amount%=500
            note100=amount//100

            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)

            t1.insert(END,str(note2000))
            t2.insert(END,str(note500))
            t3.insert(END,str(note100))

        except ValueError:
            messagebox.showerror("ERROR","Please Enter a valid number.")
    btn=Button(top,text="Calculate",command=calculator,bg="brown",fg="white")
    label.place(x=230,y=50)
    entry1.place(x=200,y=80)     
    btn.place(x=240,y=120)  
    lb.place(x=140,y=170)
    lb1.place(x=180,y=200)
    lb2.place(x=180,y=230)
    lb3.place(x=180,y=260)
    t1.place(x=270,y=200)
    t2.place(x=270,y=230)
    t3.place(x=270,y=260)
    top.mainloop()
root.mainloop()






            

