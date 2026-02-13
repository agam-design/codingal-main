import random
import string
def generatePass(length):
    characters= string.ascii_letters + string.digits + string.punctuation
    password=""

    for i in range(length):
        password+= random.choice(characters)

    return password


length=  int(input("Enter Password length:"))
print("Generate Password:", generatePass(length))