import turtle
from turtle import Turtle

class Sketch:
    turtle = Turtle()

    def forward(self):
        turtle.forward(5)

    def backward(self):
        turtle.backward(5)

    def stop(self):
        turtle.forward(5)

    def left(self):
        turtle.left(5)

    def right(self):
        turtle.right(5)

    def clear(self):
        turtle.reset()
