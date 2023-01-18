# Higher order functions
import turtle as t
from higher_order_functions import HigherOrderFunctions
from sketch_app import Sketch

# turtle = t.Turtle()
# screen = t.Screen()
# screen.listen()

# higher order start
# higher_order_function = HigherOrderFunctions()
# # screen.onkey(fun=higher_order_function.draw, key="space")
# # print(turtle.heading())
# higher order finish

# sketch app start
# sketch_app = Sketch()
# screen.onkeypress(fun=sketch_app.forward, key="w")
# screen.onkeyrelease(fun=sketch_app.stop, key="w")
# screen.onkeypress(fun=sketch_app.backward, key="s")
# screen.onkeyrelease(fun=sketch_app.stop, key="s")
# screen.onkeypress(fun=sketch_app.right, key="d")
# screen.onkeyrelease(fun=sketch_app.stop, key="d")
# screen.onkeypress(fun=sketch_app.left, key="a")
# screen.onkeyrelease(fun=sketch_app.stop, key="a")
# screen.onkey(fun=sketch_app.clear, key="c")
# sketch app finish

# screen.onkey(fun=sketch_app.forward, key="w")

#  turtle race start - my method
import random
screen = t.Screen()
turtle_list = []

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
x_value = -230
y_value = -100
color = 0
game_over = False

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

for _ in range(6):
    turtle = t.Turtle()
    turtle.shape("turtle")
    turtle.penup()
    turtle.color(COLORS[color])
    turtle.goto(x=x_value, y=-y_value)
    y_value += 40
    turtle_list.append(turtle)
    color += 1

turtle.penup()
# print(turtle_list)

turtle_count = 0

while not game_over:
    def pick_one_turtle():
        for turtle_name in turtle_list:
            turtle_name.forward(random.randint(8, 15))
            if turtle_name.xcor() > 210:
                win_turtle_color = turtle_name.color()[1]
                print(win_turtle_color)
                return [False, win_turtle_color]
        return [True]

    if not pick_one_turtle()[0]:
        break

if user_bet == pick_one_turtle()[1]:
    print(f"win: {(pick_one_turtle())[1]} - winner")
else:
    print(f"win: {pick_one_turtle()[1]} - looser")
screen.exitonclick()




