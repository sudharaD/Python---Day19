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

COLORS = ["purple", "orange", "yellow", "green", "blue", "red"]
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
    turtle.color("Black", COLORS[_])
    turtle.goto(x=x_value, y=-y_value)
    y_value += 40
    turtle_list.append(turtle)
    color += 1

turtle.penup()

print(turtle_list[1].color())
turtle_count = 0

while not game_over:
    def pick_one_turtle():
        highest_xcor = 0
        for turtle_name in turtle_list:
            turtle_name.forward(random.choice([0, 5, 10]))
        for turtle_name in turtle_list:
            if turtle_name.xcor() > highest_xcor:
                highest_xcor = turtle_name.xcor()
                win_turtle_color = turtle_name.color()[1]
        if highest_xcor > 210:
            print("a")
            # print(win_turtle_color)
            return [False, win_turtle_color]
        return [True]

    return_values = pick_one_turtle()
    if not return_values[0]:
        break

if user_bet == return_values[1]:
    print(f"win: {return_values[1]}\nYou win!")
else:
    print(f"win: {return_values[1]}\nYou loose!")
screen.exitonclick()




