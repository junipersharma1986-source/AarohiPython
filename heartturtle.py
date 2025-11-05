import turtle

# Set up screen

screen = turtle.Screen()

screen.bgcolor("white")

# Create turtle object

pen = turtle.Turtle()

pen.color("red")

pen.pensize(2)

pen.speed(1)

# Start drawing

pen.begin_fill()

pen.left(140)

pen.forward(113)

# Draw the left curve

for i in range(200):

  pen.right(1)

pen.forward(1)

# Draw the right curve

pen.left(120)

for i in range(200):

 pen.right(1)

pen.forward(1)

# Complete the shape

pen.forward(112)

pen.end_fill()

# Hide turtle and display

pen.hideturtle()

turtle.done()