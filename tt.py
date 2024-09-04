import turtle
screen = turtle.Screen()
screen.title("turtle drawing")
t= turtle.Turtle()
for _ in range(1000):
    t.circle(100)
    t.right(10)
turtle.done()