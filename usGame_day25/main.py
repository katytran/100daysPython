import turtle
from turtle import Screen, Turtle
import pandas

screen = Screen()
screen.title("U.S state Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

pen = Turtle()



data = pandas.read_csv("50_states.csv")

end_game = False
state_count = 0
while not end_game:
    answer_state = screen.textinput(title=f"{state_count}/50 correct", prompt="What's another state name")
    if state_count == 50 or answer_state.title() == "Exit":
        end_game = True
    state_row = data[data["state"] == answer_state.capitalize()]
    if len(state_row) == 0:
        pass
    else:
        state_name = state_row["state"].values
        state_xcor = state_row["x"]
        state_ycor = state_row["y"]
        pen.penup()
        pen.setpos((int(state_xcor), int(state_ycor)))
        pen.write(state_name[0], align="center")
        state_count +=1








screen.exitonclick()


