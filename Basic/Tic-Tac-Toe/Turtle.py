##### MohammadAli Mirzaei #####

import turtle  # Import the turtle module

# Create a turtle object named 'draw'
draw = turtle.Turtle()
draw.shape("turtle")  # Set the shape of the turtle to a turtle icon

# Draw a triangle
draw.goto(30, 30)  # Move the turtle to coordinates (30, 30)
draw.goto(30, -30)  # Draw a line to coordinates (30, -30)
draw.goto(0, 0)  # Draw a line back to the starting point (0, 0)

# Draw a square
draw.penup()  # Lift the pen up to move without drawing
draw.goto(-20, 35)  # Move the turtle to coordinates (-20, 35)
draw.pendown()  # Put the pen down to start drawing

for i in range(4):
    draw.forward(80)  # Move the turtle forward by 80 units
    draw.right(90)  # Turn the turtle right by 90 degrees

# Draw nested polygons
number_side = 5  # Initialize the number of sides for the polygons
x, y = -30, 70  # Set initial coordinates for drawing
side_length = 100  # Set initial side length for drawing

for i in range(5):  # Draw 5 nested polygons
    draw.penup()  # Lift the pen up to move without drawing
    draw.goto(x, y)  # Move the turtle to the current coordinates (x, y)
    draw.pendown()  # Put the pen down to start drawing

    x -= 10  # Adjust x-coordinate for the next polygon
    y += 20  # Adjust y-coordinate for the next polygon

    angle = 360.0 / number_side  # Calculate the interior angle of the polygon

    for i in range(number_side):  # Draw the polygon with the current number of sides
        draw.forward(side_length)  # Move the turtle forward by the side length
        draw.right(angle)  # Turn the turtle right by the calculated angle

    number_side += 1  # Increase the number of sides for the next polygon
    side_length += 20  # Increase the side length for the next polygon

turtle.done()  # Finish drawing and keep the window open
