# Write a Python program to - create a Tkinter window, set title to it, and set its geometry. Then add these widgets to the window - Label, Button, Entry, Frame, and a Text box
import tkinter as tk

window= tk.Tk()
window.title("Tkinter Sample window.")
window.geometry("300x300")
greeting=tk.Label(text="hello!",fg="black",bg="white")
button=tk.Button(text="click here",fg="white",bg="black")
entry=tk.Entry(fg="yellow",bg="blue",width=50)

# pack widgets
greeting.pack()
button.pack()
entry.pack()

#frame
frame=tk.Frame(master=window,relief=tk.RAISED,borderwidth=5)
frame.pack()
textBox=tk.Text(frame,fg="green",bg="yellow",height=5,width=30)
textBox.pack()

# run the main event
window.mainloop()
