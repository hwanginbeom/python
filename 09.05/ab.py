import turtle

t=turtle.Turtle()
t.shape("turtle")
t.speed(0)

t.color("red")
angle=89
for x in range(200):
    t.forward(x)
    t.left(angle)
