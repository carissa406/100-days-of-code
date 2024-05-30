#import turtle
#timmy = turtle.Turtle()
#import from the turtle module the Class of Turtle and make timmy an object

""" from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)

my_screen = Screen() #class
print(my_screen.canvheight) #attribute associated with object
my_screen.exitonclick() #function associated with screen object """

from prettytable import PrettyTable
table = PrettyTable() #new object called table from class prettytable
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = 'l'
print(table)