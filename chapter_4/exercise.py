import turtle
import math

Darsh= turtle.Turtle()

"""I'll create new fuctions for every question, just to keep track of what i did before."""

def reset_pen(t):
    """To put pen back to initial postion without doing anything else."""
    t.pu()
    t.goto((0.00,0.00))
    t.pd()

"""
Write a function called square that takes a parameter named t, which is a turtle. 
It should use the turtle to draw a square. """
def square (t):
    for i in range (4):
        t.fd(200)
        t.lt(90)

# square(Darsh)
# Darsh.fd(300)
# reset_pen(Darsh)

"""Add another parameter, named length, to square. Modify the body so length of the side is length, and then modify the fucntion call
to provide a second argurment. Run the program again. Test your program with a range of values for length.
"""
def square_2 (t, length):
    for i in range (4):
        t.fd(length)
        t.lt(90)

# square_2(Darsh, 300)
# Darsh.clear()

"""Make a copy of square and change the name to polygon. Add another parameter named n and modify the body so it draws an
n-sided regualr bolygon."""

def polygon (t, length, n):
    for i in range (n):
        t.fd(length)
        t.lt(360/n)

# polygon(Darsh, 1, 200)

"""Write a fucntion called circle that takes a turtle, t, and radius, r, an parameter
and that draws an approximate circle by calling polygon with an appropriate length and number of sides. 
Test your function with a range of values of r.

Okay so 
c =2.pi.r
c= length . n (let's fix length to 3px )
n= c/length => n= c/2  

1cm = 36px (according to google)
"""
def circle (t, r):
    """
    Arguments:
    t => turtle
    r => radius in centemeter
    """
    r= 36*r # Converting pixels into centimeter.
    c = 2*(math.pi)*r
    n = int(round(c/2, 0))
    polygon(t, 2, n)


"""Make a more genral version of circle called arc thath takes an additional parameter angle,
which determines what fraction of a circle to draw.
angle is in units of degrees, so when angen=360, arc should draw a complete circle.
arc=r.angle
"""
def polyline( t, length, n , angle):
    for i in range (n):
        t.fd(length)
        t.lt(angle)

def arc (t,r,angle):
    r= 36*r # Converting pixels into centimeter.
    c = 2*(math.pi)*r
    arc_length= c*angle/360
    n = int(round(c/50, 0))
    step_length= arc_length/n
    step_angle=angle/n

    # for i in range(n):
    #     t.fd(step_length)
    #     t.lt(step_angle) 
    
    polyline(t, step_length, n, step_angle)   


def turtle_pie (t, n):
    for i in range (n):
        polygon(t,500/n,3)
        t.lt(360/(180/n))
        


# Darsh.pu()
# Darsh.rt(90)
# Darsh.fd(10*36)
# Darsh.lt(90)
# Darsh.pd()
# polygon(Darsh,500,10)
turtle_pie(Darsh,5)



























turtle.mainloop()