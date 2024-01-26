from turtle import *
import random
import colorgram

screen = Screen()
screen.colormode(255)
# rgb_color = []
# colors = colorgram.extract('sample.webp', 6)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g ,b)
#     rgb_color.append(new_color)

color_list = [(233, 251, 243), (199, 13, 32), (250, 238, 17), (39, 76, 190)]

turtle = Turtle()
def draw_rows():
    for row in range(10):
        turtle.dot(20, random.choice(color_list))
        turtle.up()
        turtle.fd(50)
turtle.up()
turtle.hideturtle()
turtle.goto(-300, -300)
i = -300
for step in range(10):
    draw_rows()
    i = i + 50
    turtle.goto(-300, i)



screen.exitonclick()