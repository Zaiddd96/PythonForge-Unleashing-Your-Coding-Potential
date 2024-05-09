import turtle

import pandas
import pandas as pd

screen = turtle.Screen()
img = "India.gif"
turtle.Screen().addshape(img)
turtle.shape(img)
# Load the CSV file
df = pd.read_csv('50_states.csv')
state_names = df.state.tolist()
guessed = []
while len(guessed) < 30:
    guess = screen.textinput(f"{len(guessed)}/30 States correct!", "Whats the next name?").title()
    if guess == "Exit":
        missing = []
        for states in state_names:
            if states not in guess:
                missing.append(states)
        new_data = pandas.DataFrame(missing)
        new_data.to_csv("Missing_sates.csv")

        break
    if guess in state_names:
        guessed.append(guess)
        t = turtle.Turtle()
        t.penup()
        states_data = df[df.state == guess]
        t.goto(int(states_data.x), int(states_data.y))
        t.pendown()
        t.write(guess, align="center", font=("courier", 8, "normal"))
        t.hideturtle()


# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()
