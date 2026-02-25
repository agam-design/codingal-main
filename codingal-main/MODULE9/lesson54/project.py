import tkinter as tk
import random
from tkinter import*
from PIL import Image, ImageTk

root=Tk()
root.title("ROCK PAPER SCISSOR GAME")
root.geometry("400x400")
upload=Image.open(qwqwqwqwqqwwqqwqwqsqsqwwqqqgvcgjsvcdfshbbcxtsc)

choices=["ROCK","PAPER","SCISSORS"]

def play(yourChoice):
    compChoice = random.choice(choices)
    
    if yourChoice == compChoice:
        result="IT'S A TIE."
        
    elif (
        (yourChoice == "ROCK" and compChoice== "Scissors")or
        (yourChoice == "PAPERS" and compChoice== "ROCK")or
        (yourChoice == "Scissors" and compChoice== "PAPER")
    ):
        result = "YOU WIN!!"
    
    else:
        result = "COMPUTER WINS!!"
        
    yourlabel.config(text="YOU CHOSE: " + yourChoice)
    complabel.config(text="COMPUTER CHOSE: " + compChoice)
    resultlabel.config(text=result)
    
window=tk.tk()
window.title("ROCK PAPER SCISSOR GAME")
window.geometry("400x400")

title= tk.Label(window, text="CHOOSE ONE",font=("Arial",18), fg="red",bg="blue")
title.pack(pady=10)

rockBtn= tk.Button(window,text="ROCK",width=12, command=lambda:play("ROCK"),fg="black", bg="white")
rockBtn.pack(pady=5)

rockBtn= tk.Button(window, text= "Paper", width= 12,command= lambda: play("PAPER"),fg="black", bg="white")
rockBtn.pack(pady=5)

rockBtn= tk.Button(window, text="SCISSORS",width=12, command=lambda: play("SCISSORS",fg="black", bg="white"))
rockBtn.pack(pady=5)

yourlabel =tk.Label(window, text="")
yourlabel.pack(pady=5)

complabel = tk.Label(window, text="")
complabel.pack(pady=5)

resultlabel =tk.Label(window, text="", font=("Arial",18))
resultlabel.pack(pady=10)

window.mainloop()