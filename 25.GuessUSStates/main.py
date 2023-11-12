import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("US_states.csv")
all_states = data["state"].tolist()

correct_guesses = []
score = 0
game_is_on = True
while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == 'Exit':
        missing_state = [state for state in all_states if state not in correct_guesses]
        print(missing_state)
        break
    if answer_state in all_states:
        # state_data = data.index[data["state"] == answer_state].tolist()
        state_data = data[data["state"] == answer_state]
        # state_index = state_data[0]
        # xcor = data["x"][state_index]
        # ycor = data["y"][state_index]
        # coordinates = (xcor, ycor)
        temp_turtle = turtle.Turtle()
        temp_turtle.penup()
        temp_turtle.hideturtle()
        temp_turtle.goto(int(state_data["x"]), int(state_data["y"]))
        temp_turtle.write(f"{answer_state}", align="center")
        if answer_state in correct_guesses:
            pass
        else:
            correct_guesses.append(answer_state)
    print(correct_guesses)
