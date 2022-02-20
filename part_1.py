from turtle import Turtle, Screen


t = Turtle()
s = Screen()


def move_depan():
    t.forward(10)
def m_backwards():
    t.backward(10)
def c_screen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

def c_clockwise():
    new_heading = t.heading() + 10
    t.setheading(new_heading)

def clockwise():
    new_heading = t.heading() - 10
    t.setheading(new_heading)

s.listen()
s.onkey(key="w", fun=move_depan)
s.onkey(key="s", fun=m_backwards)
s.onkey(key="c", fun=c_screen)
s.onkey(key="a", fun=c_clockwise)
s.onkey(key="d", fun=clockwise)
s.exitonclick()



