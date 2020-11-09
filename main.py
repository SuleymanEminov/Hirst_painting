import turtle as t
from turtle import Screen
import random
import colorgram

# Extract colors from the image
"""
rgb_colors = []

colors = colorgram.extract('image.jpg',30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)
print(rgb_colors)

"""


# List of colors
color_list = [(198, 166, 112), (142, 78, 53), (72, 97, 123), (159, 148, 53), (214, 203, 143), (121, 38, 27),
              (137, 160, 179), (70, 108, 76), (72, 47, 40), (145, 176, 140), (194, 91, 72), (98, 82, 90), (60, 50, 54),
              (224, 177, 163), (102, 141, 130), (157, 142, 159), (97, 129, 164), (49, 61, 84), (122, 28, 31),
              (73, 68, 49), (45, 55, 72), (107, 137, 142), (181, 191, 206), (182, 199, 183), (46, 75, 64),
              (176, 96, 100)]

t.colormode(255)

pen = t.Turtle()
pen.speed("fastest")  # Speed of the pen
pen.hideturtle()  # Hide the pen
dot_size = 30  # size of dot is 30

# Move pen to a better place to improve visibility of the project
pen.setheading(220)
pen.penup()
pen.forward(308)
pen.setheading(0)


# Draws 100 dots
def draw():
    for i in range(10):
        for n in range(10):
            pen.dot(dot_size, random_color())
            pen.pen()
            pen.forward(50)
            pen.pendown()
            pen.penup()
        pen.setheading(90)
        pen.forward(50)
        pen.setheading(180)

        pen.forward(500)

        pen.setheading(0)


# Returns a random color
def random_color():
    color = random.choice(color_list)
    return color


draw() # call the main function

screen = Screen()
screen.exitonclick()
