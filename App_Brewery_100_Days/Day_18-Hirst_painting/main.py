import turtle as t
import random

# This is the part where we extract the principal rgb values, it has been run once and commented,
# the result have been manually filtered to eliminate the different white nuances and are now in "color_list" variable.

# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# extracted_colors = []
# for color in colors:
#     red = color.rgb.r
#     green = color.rgb.g
#     blue = color.rgb.b
#     output = (red, green, blue)
#     extracted_colors.append(output)
#
# print(extracted_colors)

color_list = [
    (132, 166, 205), 
    (221, 148, 106), 
    (32, 42, 61), 
    (199, 135, 148), 
    (166, 58, 48), 
    (141, 184, 162),
    (39, 105, 157), 
    (237, 212, 90), 
    (150, 59,66), 
    (216, 82, 71), 
    (168, 29, 33), 
    (235, 165, 157),
    (51, 111, 90), 
    (35, 61, 55), 
    (156, 33, 31), 
    (17, 97, 71), 
    (52, 44, 49), 
    (230, 161, 166),
    (170, 188, 221), 
    (57, 51, 48), 
    (184, 103, 113),
    (32, 60, 109), 
    (105, 126, 159), 
    (175, 200, 188),
    (34, 151, 210), 
    (65, 66, 56)
    ]

tim = t.Turtle()
t.colormode(255)
screen = t.Screen()
screen.setup(width=700, height=700, startx=0, starty=0)
screen.bgcolor(255, 255, 255)
tim.up()
tim.speed("fastest")
tim.hideturtle()


def new_dot():
    """print a new dot"""
    tim.color(random.choice(color_list))
    tim.begin_fill()
    tim.circle(15)
    tim.end_fill()
    tim.fd(70)


def new_line():
    for dot in range(10):
        new_dot()


def new_draw():
    for line in range(10):
        tim.setx(-325)
        tim.sety(25 + (line-5)*70)
        new_line()


def export(nb):
    ts = t.getscreen()
    ts.getcanvas().postscript(file=f"test-{nb}.ps")


for number in range(10):
    new_draw()
    export(number)
    t.reset()


screen.exitonclick()
