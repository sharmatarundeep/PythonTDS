# Turtle is used for graphical programming
# It is representation of a physical “turtle” (a little robot with a pen) that draws.
# Turtle is a pointer which starts in the center and you can say go forward, use red color pen, fill in color, move left etc

import turtle 
import random

def turtle_triangle():
    turtle.color("green") #Use red color for drawing
    turtle.forward(100) #Send turtle 100 steps forward, right is the default direction of move
    turtle.left(120) #Change the direction to 120 degree, basically take 120 degree turn
    turtle.forward(100)
    turtle.left(120) 
    turtle.forward(100)
    turtle.done() # to see the image and end the process

def turtle_square():
    turtle.color("red", "blue") #Use red color for drawing boundary and blue color to fill in
    turtle.begin_fill() #Do this before starting the drawing, if you want to fill in color
    turtle.forward(100) #Send turtle 100 steps forward, right is the default direction of move
    turtle.left(90) #Change the direction to 90 degree, basically take 90 degree turn
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.end_fill() #Do this after the drawing instructions are completed
    turtle.done() # to see the image and end the process

def turtle_two_squares(turtle_object):
    #draw first square
    turtle_object.color("blue", "red") #Use red color for drawing boundary and blue color to fill in
    turtle_object.begin_fill() #Do this before starting the drawing, if you want to fill in color
    turtle_object.forward(100) #Send turtle 100 steps forward, right is the default direction of move
    turtle_object.left(90) #Change the direction to 90 degree, basically take 90 degree turn
    turtle_object.forward(100)
    turtle_object.left(90)
    turtle_object.forward(100)
    turtle_object.left(90)
    turtle_object.forward(100)
    turtle_object.end_fill() #Do this after the drawing instructions are completed
    
    #pen up, move 100 steps down and pen down
    turtle_object.penup()# to avoid drawing the move line
    turtle_object.forward(100) # After first square is done, go 100 steps forward (down in this case as last direction was towards down) and draw another square
    turtle_object.pendown()# after moving 100 steps lets put the pen down

    # start drawing the second square
    turtle_object.color("blue", "red") #Use red color for drawing boundary and blue color to fill in
    turtle_object.begin_fill() #Do this before starting the drawing, if you want to fill in color
    turtle_object.forward(100) #Send turtle 100 steps forward, right is the default direction of move
    turtle_object.left(90) #Change the direction to 90 degree, basically take 90 degree turn
    turtle_object.forward(100)
    turtle_object.left(90)
    turtle_object.forward(100)
    turtle_object.left(90)
    turtle_object.forward(100)
    turtle_object.end_fill() #Do this after the drawing instructions are completed

    turtle.done() # to see the image and end the process


#turtle_square()
#turtle_triangle()

#t = turtle.Turtle() #using turtle object
#t.getscreen().bgcolor("black") # set the output screen back ground color
#turtle_two_squares(t)'''
    
# Build a star
t = turtle.Turtle() #using turtle object
def draw_star(turtle_object, size):
    t.getscreen().bgcolor("black") # set screen background color to black
    t.color("white", "yellow") # color for star drawing
    t.speed(20) # to speed up the drawing
    for _ in range(5): # for nothing in range 5 , when you don't want to use the variable value in range
        turtle_object.forward(size)
        turtle_object.left(216) # this is the needed angle for star

# draw_star(t,100) # create one start
        
# Now if you want to create sky full of 50 stars
for _ in range (50): # 50 stars
    # x and y coordinates of the screen for where to make the star
    x=random.randint(-300,300)
    y=random.randint(-300,300) # center of screen is 0,0. If you go left + up its negative. If you go right and down its positive

    t.penup()
    t.goto(x,y) # go to the coordinates
    t.pendown()
    t.begin_fill()
    draw_star(t,random.randint(5,50)) # random size of the star
    t.end_fill()