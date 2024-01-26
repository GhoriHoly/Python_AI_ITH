from turtle import *
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("tomato")

sides = 3
# colors = ["red","green","blue","purple","black","yellow","orange","navy blue"]
# Age list theke color niye change korsilam. ekhon random RGB color use korbe turtle
# directions = [0, 90, 180, 270]



# screen object age create kore felte hobe. ar na hole colormode use kora jabena.
screen = Screen()
screen.colormode(255)
timmy_the_turtle.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)

    return random_color


for _ in range(100):
    timmy_the_turtle.width(2)
    # timmy_the_turtle.forward(100)
    timmy_the_turtle.circle(100, 360, 90)
    # timmy_the_turtle.color(random.choice(colors))
    timmy_the_turtle.color(random_color())
    stamp_id = timmy_the_turtle.stamp()
    timmy_the_turtle.rt(5)


timmy_the_turtle.home()

screen.exitonclick()
