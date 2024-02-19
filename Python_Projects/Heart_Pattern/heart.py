# We will use turtle module to create the heart

import turtle

turtle.pensize(5) # setting up the pensize , width of pen for drawing
turtle.speed(5) # setting up the speed of drawing
turtle.color("Black") # setting up the boundary color
turtle.begin_fill()
turtle.fillcolor("red") # setting up the fill color
turtle.left(150) # change direction
turtle.forward(180)
turtle.circle(-90,180) # make a semicircle
turtle.setheading(60) # change the head/pen direction 
turtle.circle(-90,180) # make a semicircle
turtle.forward(180)
turtle.end_fill()

# to write something inside the heart
turtle.penup()
turtle.goto(-100,100)
turtle.pendown()
turtle.write("LOVE",font=("verdana", 25, "bold"))
turtle.done() # to keep the image open