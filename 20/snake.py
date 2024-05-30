from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT= 180
RIGHT = 0
    
class Snake():

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        x_coord = 0
        for _ in range(0,3):
            new_turtle = Turtle(shape='square')
            new_turtle.color('white')
            new_turtle.penup()
            new_turtle.goto(x_coord, 0)
            self.segments.append(new_turtle)
            x_coord -= 20
    
    def move(self):
        for seg_num in range(len( self.segments)-1, 0, -1):
            new_x =  self.segments[seg_num - 1].xcor()
            new_y =  self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE) 

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)