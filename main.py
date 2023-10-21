import turtle
import pandas
style = ('Courier', 10, 'italic')
screen = turtle.Screen()
screen.title("US State guessing game")
image = "blank_states_img.gif"
screen.addshape(image)
data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()
answered = []
turtle.shape(image)
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
game = True
i = 0
while game:
    if i >= 50:
        print("You've guessed all US states")
        break
    answer_state = screen.textinput(title=f"{50-i} states remaining", prompt="Guess a state in US: ")
    answer_state = answer_state.title()
    if answer_state == "Exit":
        game = False
        break
    if answer_state in state_list:
        if answer_state not in answered:
            row = data[data["state"] == answer_state]
            xcor = int(row["x"].iloc[0])
            ycor = int(row["y"].iloc[0])
            writer.goto(xcor, ycor)
            writer.write(answer_state, font=style, align="center")
            answered.append(answer_state)
            print("Good")
            i += 1
        else:
            print("You've already guessed that state")
    else:
        print("That is not a US state")
screen.exitonclick()