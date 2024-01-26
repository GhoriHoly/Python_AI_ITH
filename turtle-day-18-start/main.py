from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("tomato")

sides = 3
colors = ["red","green","blue","purple","black","yellow","orange","navy blue"]
i = 0
for _ in range(8):
    for _ in range(sides):
        cones = 360 / sides
        timmy_the_turtle.color(colors[i])
        timmy_the_turtle.width(5)
        timmy_the_turtle.left(cones)
        timmy_the_turtle.forward(100)

    sides +=1
    i+= 1


timmy_the_turtle.home()


screen = Screen()
screen.exitonclick()