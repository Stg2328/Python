import turtle
from turtle import Screen,Turtle
import random


screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title="make your bet",prompt="Choice Your Color Of Turtle :")
print(user_bet)
colors = ["red","green","pink","blue","orange","black"]
positions = [-70,-40,-10,20,50,80]
all_tutles = []
print(colors)
for turtle_index in range(6):
    tin = Turtle()
    tin.shape("turtle")
    tin.color(colors[turtle_index])
    tin.penup()
    tin.goto(x=-240,y=positions[turtle_index])
    all_tutles.append(tin)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtles in all_tutles:
        if turtles.xcor() > 230:
            is_race_on = False
            winning_color = turtles.pencolor()
            if winning_color == user_bet:
                print(f"You are winning the your {winning_color} turtle")
            else:
                print(f"You are Lost the winning color is {winning_color} turtle")
        random_distance = random.randint(0,10)
        turtles.forward(random_distance)





screen.exitonclick()