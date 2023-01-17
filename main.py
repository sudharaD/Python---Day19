# Higher order functions
import turtle as t
from higher_order_functions import HigherOrderFunctions

turtle = t.Turtle()
screen = t.Screen()
screen.listen()

higher_order_function = HigherOrderFunctions()

screen.onkey(fun=higher_order_function.draw, key="space")

screen.exitonclick()

