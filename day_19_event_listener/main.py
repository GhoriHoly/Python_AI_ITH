import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def move_anticlockwise():
  # heading actually move the arrow head in any direction

  new_heading = tim.heading() + 10
  tim.setheading(new_heading)


def move_clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.up()
    tim.home()
    tim.down()

screen.listen()

screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_clockwise, "a")
screen.onkey(move_anticlockwise, "d")
screen.onkey(clear, "c")

screen.exitonclick()
