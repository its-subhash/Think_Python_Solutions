import turtle
import math

# #Down arrow
bob= turtle.Turtle()

def down_arrow(t):
    t.pu()
    t.bk(100)
    t.pd()
    t.rt(45)
    t.fd(141.4213562373095)
    t.lt(90)
    t.fd(141.4213562373095)
    t.lt(135)
    t.fd(50)
    t.rt(90)
    t.fd(200)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(200)
    t.rt(90)
    t.fd(50)

def square(t, width, length):
        t.fd(width)
        t.lt(90)
        t.fd(length)
        t.lt(90)
        t.fd(width)
        t.lt(90)
        t.fd(length)
        t.lt(90)

def cube(t, width,length, short_side):
    square(bob,width, length)
    t.lt(45)
    t.forward(short_side)
    t.right(45)
    square(bob,width, length)
    t.forward(width)
    t.right(135)
    t.forward(short_side)
    t.right(180)
    t.forward(short_side)
    t.left(45)
    t.forward(length)
    t.left(135)
    t.forward(short_side)
    t.right(45)
    t.forward(width)
    t.right(135)
    t.forward(short_side)

# cube(bob, 30, 300,15)


turtle.mainloop()
