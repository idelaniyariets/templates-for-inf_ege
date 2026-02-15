from turtle import *

tracer(0)
m = 5
screensize(10000, 10000)

for i in range(5):
    fd(40 * m)
    rt(90)
    fd(46 * m)
    rt(90)

up()
fd(19 * m)
rt(90)
fd(19 * m)
lt(90)
down()

for i in range(5):
    fd(37 * m)
    rt(90)
    fd(19 * m)
    rt(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*m, y*m)
        dot(3, "red")
update()
exitonclick()