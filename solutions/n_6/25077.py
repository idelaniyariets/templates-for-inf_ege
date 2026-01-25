from turtle import *

tracer(0)
m = 10
screensize(10000, 10000)
down()

rt(180)
for i in range(2):
    fd(30 * m)
    lt(90)
    fd(15 * m)
    lt(90)
up()

fd(5*m)
rt(90)
fd(8 * m)
lt(90)
down()

for i in range(5):
    fd(12 * m)
    lt(90)
    fd(31 * m)
    lt(90)
up()

for i in range(2):
    lt(90)
    fd(8 * m)
    rt(90)
    fd(4*m)
    lt(90)
down()

for i in range(4):
    fd(16*m)
    lt(90)
up()

goto(0,0)
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*m, y*m)
        dot(3, "red")

update()
exitonclick()