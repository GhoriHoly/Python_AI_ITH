import time
from turtle import Screen, Turtle

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('My Snake Game')

screen.tracer(0)


# Create snake-------------------
snake_body = []
separation = 0
for tim in range(0, 3):
        tim = Turtle()
        tim.shape('square')
        tim.color('white')

        tim.penup()
        tim.goto(0 + separation, 0 )
        separation = separation - 20
        snake_body.append(tim)



# ----------------------------------



# Move snake------------------------
game_is_on = True
while game_is_on:
        screen.update()
        # 1 sec delay between each movement. Must import time module
        time.sleep(0.1)
        for snake_part in range(len(snake_body)-1,0,-1):
                new_x = snake_body[snake_part -1].xcor()
                new_y = snake_body[snake_part-1].ycor()
                snake_body[snake_part].goto(new_x,new_y)
        snake_body[0].forward(20)






screen.exitonclick()