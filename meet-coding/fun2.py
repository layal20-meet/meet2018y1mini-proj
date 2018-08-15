import turtle
turtle.goto(0,0)

UP = 0
RIGHT =1 
direction = None
def up():
    global direction
    print("you pressed the up key")
    direction = UP
    on_move()

def right():
    print("you pressed the right key")
    global direction
    direction = RIGHT
    on_move()
turtle.listen()

