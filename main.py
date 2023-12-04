from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# Event Management functions
# Press functions
def move_forwards():
    tim.forward(10)

def turn_left():
    tim.left(10)

def move_backwards():
    tim.backward(10)

def turn_right():
    tim.right(10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen() # Necessary before adding Event Listeners

# Event Listeners
screen.onkeypress(key="w", fun=move_forwards) # IMPORTANT not to add () at the end of the func name so it only executes when the key is pressed
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="d", fun=turn_right)
screen.onkeypress(key="c", fun=clear_screen)

screen.exitonclick()