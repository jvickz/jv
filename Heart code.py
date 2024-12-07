import turtle
import math

t = turtle.Turtle()
t.speed(0)
t.color("red")
turtle.bgcolor("pink")


def corazon(n):
    x = 16 * math.sin(n) ** 3
    y = 13 * math.cos(n) - 5 * \
        math.cos(2*n) - 2*math.cos(3*n) - \
        math.cos(4*n)
    return x, y


t.penup()
for i in range(15):
    t.goto(0, 0)
    t.pendown()
    for n in range(0, 100, 2):
        x, y = corazon(n/10)
        t.goto(x*i, y*i)
    t.penup

t.goto(0, -20)  # posciona a tartaruga no meio
t.color("green")
t.write("JV ", align="center", font=("Arial", 20, "bold"))

t.hideturtle()
turtle.done()
