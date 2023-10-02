import colorgram 
import turtle as t
import random

# raw_colors = colorgram.extract('Day 18/Vipera-Lebetina-by-Damien-Hirst.jpg', 30)

# rgb_colors = []
# for color in raw_colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

color_list = [(204, 183, 148), (191, 203, 212), (208, 202, 144), (192, 211, 201), (211, 195, 202), (212, 178, 191), (174, 201, 189), (180, 191, 185), (172, 180, 200), (218, 179, 170), (196, 178, 191), (169, 190, 217), (177, 200, 203)]

#create painting with 10 x 10 rows of spots
#size 20, space 50

t.colormode(255)
tim = t.Turtle()

def line_of_dots():
    for _ in range(10):
        tim.color(random.choice(color_list))
        tim.penup()
        tim.forward(50)
        tim.dot(20)

x = 0
for i in range(10):
    x+=50
    line_of_dots()
    tim.setposition(0, x)

screen = t.Screen()
screen.exitonclick()