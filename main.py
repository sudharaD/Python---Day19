# Higher order functions
import turtle as t
from higher_order_functions import HigherOrderFunctions
from sketch_app import Sketch

turtle = t.Turtle()
screen = t.Screen()
screen.listen()

# higher_order_function = HigherOrderFunctions()
# # screen.onkey(fun=higher_order_function.draw, key="space")
# # print(turtle.heading())

sketch_app = Sketch()
screen.onkeypress(fun=sketch_app.forward, key="w")
screen.onkeyrelease(fun=sketch_app.stop, key="w")
screen.onkeypress(fun=sketch_app.backward, key="s")
screen.onkeyrelease(fun=sketch_app.stop, key="s")
screen.onkeypress(fun=sketch_app.right, key="d")
screen.onkeyrelease(fun=sketch_app.stop, key="d")
screen.onkeypress(fun=sketch_app.left, key="a")
screen.onkeyrelease(fun=sketch_app.stop, key="a")
screen.onkey(fun=sketch_app.clear, key="c")

# screen.onkey(fun=sketch_app.forward, key="w")

screen.exitonclick()

