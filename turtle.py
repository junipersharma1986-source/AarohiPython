import turtle

# Set up the screen

screen = turtle.Screen()

screen.bgcolor("lightblue") # Background color

# Create turtle object

polygon = turtle.Turtle()

polygon.color("darkgreen") # Pen color

polygon.pensize(3) # Pen thickness

# Polygon settings

num_sides = 3 # Change this for triangle (3), square (4), etc.

side_length = 100

angle = 360 / num_sides # Angle between sides

# Draw the polygon

for i in range(num_sides):

    polygon.forward(side_length)

    polygon.right(angle)

# Finish

turtle.done()