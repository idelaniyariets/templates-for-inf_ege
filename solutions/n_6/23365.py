from turtle import *

tracer(0)
m = 5
screensize(10000, 10000)

for i in range(3):
    fd(39*m)
    rt(90)
    fd(48*m)
    rt(90)
up()
fd(27 *m)
rt(90)
fd(24 * m)
lt(90)
down()

for i in range(3):
    fd(29 * m)
    rt(90)
    bk(18*m)
    rt(90)
up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*m, y*m)
        dot(3, "red")

update()
exitonclick()