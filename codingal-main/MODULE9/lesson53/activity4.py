import tkinter as tk
import random

choices= ["Rock", "Paper", "Scissors"]

def play(yourChoice):
    compChoice = random.choice(choices)

    if yourChoice == compChoice:
        result ="It's a Tie"

    elif (
        (yourChoice == "Rock" and compChoice == "Scissors")or
        (yourChoice == "Paper" and compChoice == "Rock")or
        (yourChoice == "Scissors" and compChoice == "Paper")
    ):
        result = "You Win!!"
    
    else:
        result = "Computer Wins!!"

    yourlabel.config(text="You Chose: " + yourChoice)
    complabel.config(text="Computer chose: " + compChoice)
    resultlabel.config(text=result)

window =tk.Tk()
window.title("Rock Paper Scissors Game")
window.geometry("300x300")

title= tk.Label(window, text="Choose One", font=("Arial",16), fg="navyblue", bg="grey")
title.pack(pady=10)

rockBtn= tk.Button(window, text ="Rock", width= 10, command=lambda: play("Rock"),fg="white" , bg="black")
rockBtn.pack(pady=5)

rockBtn= tk.Button(window, text ="Paper", width= 10, command=lambda: play("Paper"),fg="purple", bg="black")
rockBtn.pack(pady=5)

rockBtn= tk.Button(window, text ="Scissors", width= 10, command=lambda: play("Scissors"),fg="green", bg="black")
rockBtn.pack(pady=5)

yourlabel = tk.Label(window, text="")
yourlabel.pack(pady=5)

complabel = tk.Label(window, text="")
complabel.pack(pady=5)

resultlabel = tk.Label(window, text="", font=("Arial",14))
resultlabel.pack(pady=10)

window.mainloop()