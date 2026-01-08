import turtle 

# Set up screen
screen = turtle.Screen()
screen.bgcolor("blue")
screen.title("Welcome to Turtle window")

board = turtle.Turtle()

# creating equilateral triangle
for _ in range(3):
    board.forward(100)
    board.left(120)

# Move turtle to a new position for rectangle
board.penup()
board.goto(-250,-100)
board.pendown()

# creating a rectangle
for i in range(2):
    board.fillcolor("red")
    board.begin_fill()
    board.forward(200)
    board.left(90)
    board.forward(100)
    board.left(90)
    board.end_fill()

#moving turtle to a new position for hexagon
board.penup()
board.goto(200,100)
board.pendown()


#creating hexagon
for i in range(6):
    board.forward(100)
    board.right(60)

# Finish drawing
turtle.done()
