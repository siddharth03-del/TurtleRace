from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(height=400, width=600)
colors = ['purple', 'orange', 'red', 'green', 'yellow', 'blue']
all_turtles = []
coordinates = [-100, -50, 0, 50, 100, 150]
race_on = False
for i in range (6):
    new_turtle = Turtle()
    new_turtle.shape('turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-280, coordinates[i])
    all_turtles.append(new_turtle)

user_choice = screen.textinput(title="Choose a turtle", prompt="Choose a turtle color you think will win this race..")
race_on = True
while race_on:
    for turtle in all_turtles:
        if(turtle.xcor() > 290):
            race_on = False
            winner = turtle.color()
            break
        else:
            turtle.forward(random.randint(0,10))
if(user_choice == winner[0]):
    print(f"Your guess was right your turtle {user_choice} won the race")
else:
    print(f"Oh no! The {winner[0]} won the race")

screen.exitonclick()