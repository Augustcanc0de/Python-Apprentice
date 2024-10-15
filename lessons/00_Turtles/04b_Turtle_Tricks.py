"""
For this program, you will tell Tina the Turtle to draw 
a pentagon.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.

"""


import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)
tina = turtle.Turtle()

tina.shape('turtle')                   
tina.speed(1)                          

tina.pencolor('cyan')
tina.forward(45)
tina.left(45)

tina.pencolor('cyan')
tina.forward(45)
tina.left(45)

tina.pencolor('cyan')
tina.forward(45)
tina.left(45)

tina.pencolor('cyan')
tina.forward(45)
tina.left(45)

tina.pencolor('cyan')
tina.forward(45)
tina.left(45)

tina.pencolor('cyan')
tina.forward(45)
tina.left(45)

tina.pencolor('cyan')
tina.forward(45)
tina.left(45)

tina.pencolor('cyan')
tina.forward(45)
tina.left(45)

turtle.exitonclick()                    # Close the window when we click on it


