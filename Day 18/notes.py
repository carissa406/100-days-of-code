
import turtle as t
import random

""" from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green") """
#drawing a square
""" for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)

#drawing a dotted line
for _ in range(5):
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown() """

#colors = ["red", "blue", "orange", "yellow", "green", "blue", "purple"]
#drawing shapes inside shapes
""" num_sides=4
def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)

for shape_side_n in range(3, 21):
    timmy_the_turtle.color(random.choice(colors))
    draw_shape(shape_side_n)

 """

#drawing random directions random colors
tim = t.Turtle()
tim.pensize(1)
tim.speed(0)
directions = [0, 90, 180, 270]

t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return(r, g, b)

""" for _ in range(200):
    tim.pencolor(random_color())
    tim.forward(30)
    tim.seth(random.choice(directions))
 """
def draw_spiro(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spiro(5)

screen = t.Screen()
screen.exitonclick()