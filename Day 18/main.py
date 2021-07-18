import turtle
import colorgram, random


# this is a code to mimic a Damien Hirst spot painting. 


# set the color mode to 255 to use RGB color scheme
turtle.colormode(255)

# set the screen object to change the coordinates and use exitonclick()
screen = turtle.Screen()
screen.setworldcoordinates(-100,-100,550,550)

# create a turtle object,and penup to remove the lines, and hideturtle to not show the turtle icon
tommy = turtle.Turtle()
tommy.penup()
tommy.hideturtle()


# using colorgram module to extract the colors from an image. 
# make sure to keep the image in the same folder as the code. 
colors = colorgram.extract('image.jpg',30)
rgb_colors = []

# converting the list of colors to rgb values. 
# excluding the first 5 here as this is a demo for Damien hirst spot painting and we get the background colors
for color in colors[5:]:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb = (r,g,b)
    rgb_colors.append(rgb)

# loop ten x ten times and print dots. 
y_axis = 0
for i in range(10): 
    for j in range(10):
        tommy.dot(15, random.choice(rgb_colors))
        tommy.forward(50)

    tommy.home()
    y_axis += 50
    tommy.sety(y_axis)


# to keep displaying the turtle screen until a click
screen.exitonclick()
