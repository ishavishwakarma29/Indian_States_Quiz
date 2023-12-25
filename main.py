import turtle
import pandas

screen = turtle.Screen()
screen.title("Indian States Game")
screen.setup(width=550, height=600)
img="blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv("29_states.csv")
states = data["state"].to_list()
# print(states)
guessed = []

t=turtle.Turtle()
t.hideturtle()
t.penup()
t.goto(110,240)
t.write('Enter "Exit" to end the quiz \n You can drag the input box', align="center", font=("Arial", 16, "normal"))

while len(guessed) < 29:
    user_input = screen.textinput(title=f"{len(guessed)}/29 guessed", prompt="What's another state?").title()

    # correct guess
    if user_input=="Exit":
        missing_states = []
        for state in states:
            if state not in guessed:
                missing_states.append(state)
        break
    if user_input.title() in states:
        guessed.append(user_input)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"]==user_input.title()]
        t.goto(int(state_data.x), int(state_data.y))
        t.pencolor("blue")
        t.write(user_input.title())

# states to learn


screen.clear()
t = turtle.Turtle()
t.hideturtle()
t.penup()

if len(guessed) == 29:
    t.write("Congratulations you have guessed all the Indian states.", align="center", font=("Arial", 16, "normal"))

else:
    t.write(f"You have guessed {len(guessed)} states out of 29 Indian states", align="center", font=("Arial", 16, "normal"))

screen.exitonclick()