import turtle
import random

screen = turtle.Screen()
screen.setup(800,600)
is_race_on = False
user_bet = screen.textinput(title="Make Your Bet.", prompt="Guess a turtle color that'll win!")
colors = ["red", "blue", "purple", "yellow", "green", "orange"]

all_turtles = []
# Creating Turtles and setting their positions with different colors.
def turtles():
    y_val = -150
    for index in range(0, 6):
        tim = turtle.Turtle("turtle")
        tim.up()
        tim.color(colors[index])
        tim.goto(x=-350, y=y_val)
        index += 1
        y_val += 50
        all_turtles.append(tim)
turtles()
# To start the race
if user_bet:
    is_race_on = True

while is_race_on:
    for turtles in all_turtles:
        random_dist = random.randint(0, 10)
        turtles.forward(random_dist)
        # Checking if turtles any touches the end point.
        if turtles.xcor() > 370:
            winning_color = turtles.pencolor()
            # Checking which turtle finished the race first.
            if winning_color == user_bet.lower():
                screen.textinput(title="Winner", prompt="You Won!")
            else:
                screen.textinput(title="Loser", prompt="You Lose!")
            is_race_on = False
screen.exitonclick()
