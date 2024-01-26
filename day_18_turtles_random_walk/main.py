from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("tomato")

sides = 3
colors = ["red","green","blue","purple","black","yellow","orange","navy blue"]
directions = [0,90,180,270]
timmy_the_turtle.speed("slow")
for _ in range(200):
    timmy_the_turtle.width(10)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.setheading(random.choice(directions))
    timmy_the_turtle.color(random.choice(colors))

timmy_the_turtle.home()


screen = Screen()
screen.exitonclick()