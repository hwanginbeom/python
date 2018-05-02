import turtle as t
t.shape("turtle")
t.color("red")
t.speed(0)
import random
y=random.randint(1,360)
print("y=" , y)

for x in range(500):
    t.forward(x)
    t.right(y)
