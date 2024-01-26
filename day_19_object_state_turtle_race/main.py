from turtle import Turtle, Screen
import random

turtle = Turtle()
screen = Screen()

screen.setup(500, 400)
user_bet = screen.textinput("Make your bet.", "Which turtle will winn? Enter a color: ")

colors = ['red','green','blue','yellow', 'orange','purple']
all_turtles = []
is_race_on = False
i = 0
separation = 0
for _ in range(0, 6):
    tim = Turtle('turtle')
    tim.color(colors[i])
    i = i + 1
    tim.penup()
    tim.goto(-230, -100 + separation)
    separation = separation + 30
    all_turtles.append(tim)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! and the {winning_color} turtle is the winner. ")
            else:
                print(f"You've lose. and the {winning_color} turtle is the winner.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()