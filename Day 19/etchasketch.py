from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.backward(10)
def move_counterclockwise():
    tim.left(10)
def move_clockwise():
    tim.right(10)
def clear_drawing():
    screen.resetscreen()

screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=move_counterclockwise)
screen.onkey(key='d', fun=move_clockwise)
screen.onkey(key='c', fun=clear_drawing)




screen.exitonclick()