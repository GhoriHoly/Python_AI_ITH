import turtle
import pandas
screen = turtle.Screen()

screen.title("U.S States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guesses_state = []

while len(guesses_state) < 50:
    answer = screen.textinput(f"{len(guesses_state)}/50 States Correct", "What's another state name?").title()
    if answer == 'Exit':
        missing_states = []
        for state in all_states:
            if state not in guesses_state:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break

    if answer in all_states:
        # Each time user guess correctly we add to the list.
        guesses_state.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # Fetching the correct row data.
        state_data = data[data.state == answer]
        xc = int(state_data.x.item())
        yc = int(state_data.y.item())
        t.goto(xc, yc)
        # item() is used to just get the data not other things of the DataFrame.
        t.write(answer)












screen.exitonclick()