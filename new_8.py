import turtle

screen = turtle.Screen()
screen.setup(width=400, height=700)
screen.bgcolor("black")

colors = ["#ED9121", "#FF7518"]
t = turtle.Turtle()
t.speed(0); t.hideturtle()

def square(side_length, angle):
    for _ in range(4):
        t.forward(side_length); t.right(angle)

for i in range(360):
    t.pencolor(colors[i % 2])

    square(100, 90)
    square(120, 90)

    t.circle(25); t.right(3); t.circle(25)
    t.right(5)

screen.done()