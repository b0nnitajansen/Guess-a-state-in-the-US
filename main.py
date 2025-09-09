import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
guessed_states = []
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
correct_guesses = 0

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

while len(guessed_states) < 50:
    user_answer = screen.textinput(title=f"Guess the state {correct_guesses}/50",
                                     prompt="What's another state's name?").strip().title()
    if user_answer == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        pandas.DataFrame(missing_states).to_csv("states_to_learn.csv")
        break

    if user_answer in all_states:
        guessed_states.append(user_answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == user_answer]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(user_answer)
        correct_guesses += 1

screen.exitonclick()
