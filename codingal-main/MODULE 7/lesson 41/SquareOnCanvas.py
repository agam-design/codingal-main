import turtle
turtle.Screen().bgcolor("Orange")

sc=turtle.Screen()
sc.setup(400,300)

turtle.title("Welcome to Turtle window")

board=turtle.Turtle()

#creating a square
for i in range(4):
    board.forward(100)#side length
    board.left(90)#angle of aquare
    i=i+1
