#let's import the required module

import turtle

# here we set the color of screen to display

window = turtle.Screen()

window.bgcolor("black")

# now lets set the stroke 

ink = turtle.Turtle()

ink.hideturtle()

ink.width(4)

ink.color("white")

# here we will add a prompt box to choose the shape

shape = turtle.textinput("Enter the respective number of shape", "1 - line \n 2 - acute angle \n 3 - triangle\n 4 - square\n 5 - pentagon\n 6 - hexagon\n 7 - heptagon\n 8 - octagon\n 9 - nonagon\n 10 - decagon")

#first let's make a straight line

if shape == "1":

	ink.forward(100)

#this is to draw an acute angle	

elif shape == "2":

	for i in range(2):

		ink.forward(100)

		ink.left(90)

#this is to draw a triangle		

elif shape == "3":

	for i in range(3):

		ink.forward(100)

		ink.left(120)

#this is to draw a square		

elif shape == "4":

	for i in range(4):

		ink.forward(100)

		ink.left(90)

#this is to draw a pentagon		

elif shape == "5":

	for i in range(5):

		ink.forward(100)

		ink.left(72)

#this is to draw a hexagon		

elif shape == "6":

	for i in range(6):

		ink.forward(100)

		ink.left(60)

#this is to draw a heptagon		

elif shape == "7":

	for i in range(7):

		ink.forward(100)

		ink.left(52)

#this is to draw a octagon		

elif shape == "8":

	for i in range(8):

		ink.forward(100)

		ink.left(45)

#this is to draw a nonagon		

elif shape == "9":

	for i in range(9):

		ink.forward(100)

		ink.left(40)

# and finally to draw a decagon		

elif shape == "10":

	for i in range(10):

		ink.forward(100)

		ink.left(36)

# here our programme is finished

turtle.done()
