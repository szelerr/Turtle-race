from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet", prompt="Who will win the race? Add one of the rainbow colours:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []


def setup_turtles():
    start_position = 80
    for i in range(0, 6):
        tim = Turtle("turtle")
        turtles.append(tim)
        tim.color(colors[i])
        tim.penup()
        tim.goto(-240, start_position)
        start_position -= 30


def random_movement(rand_turtle, movement):
    rand_turtle.forward(movement)


setup_turtles()
is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winner = turtle.fillcolor()
            is_race_on = False

    random_distance = randint(0, 10)
    random_turtle = randint(0, len(turtles) - 1)
    random_movement(turtles[random_turtle], random_distance)

if winner == user_bet:
    print("You win the bet!")
else:
    print(f"You lose. The winner is {winner}")

screen.exitonclick()
