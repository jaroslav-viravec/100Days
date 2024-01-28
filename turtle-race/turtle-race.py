from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Winner", prompt="Which turtle will win the race? Enter the color: ")
colors = ["red", "orange", "magenta", "green", "blue", "purple"]
all_turtles = []
y_position = 0

for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.goto(x=-230, y=-100 + y_position)
    y_position += 30
    turtle.color(color)
    all_turtles.append(turtle)
    
if user_input:
    is_race_on = True
while is_race_on:
    for t in all_turtles:
        if t.xcor() > 230:
            is_race_on = False
            winning_color = t.pencolor()
            if winning_color == user_input:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You lost! The {winning_color} turtle is the winner")
        random_distance = random.randint(0,10)
        t.forward(random_distance)    
screen.exitonclick()
