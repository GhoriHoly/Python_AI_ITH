# from turtle import *
from prettytable import PrettyTable

"""timmy is my varible name for my turtle object Turtle() is the class imported from turtle"""
# timmy = Turtle()

"""Slash should be used from numberpad of the keyborad. SO TO COMMENT USE Ctrl+/"""
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
#
# print(timmy)

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmandar"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align["Pokemon Name"] = "l"
table.align["Type"] = "r"
print(table)


# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

