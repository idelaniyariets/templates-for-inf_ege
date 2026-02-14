from turtle import *

tracer(0)
m = 5
screensize(10000, 10000)

for i in range(2):
    fd(3*m)
    rt(90)
    fd(20*m)
    rt(90)
up()
bk(8*m)
rt(90)
fd(9*m)
lt(90)
down()
for i in range(2):
    fd(16*m)
    rt(90)
    fd(8*m)
    rt(90)
up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*m, y*m)
        dot(3, "red")
update()
exitonclick()