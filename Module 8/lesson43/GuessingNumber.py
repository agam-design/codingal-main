import random

def game():
    number = random.randint(1,50)
    guess = 0
     
    print("guess a number between 1 and 50")

    while guess != number:
        guess =int(input("enter your guess: "))
        if guess < number:
           print("too low")
        elif guess > number:
            print("too high")
        else:
            print("correct! you guessed it.")
game()

