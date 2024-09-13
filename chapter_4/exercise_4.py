import turtle

darsh= turtle.Turtle()

def polyline( t, length, n , angle):
    for i in range (n):
        t.fd(length)
        t.lt(angle)

def arc (t,r,angle):
    c = 2*(math.pi)*r
    arc_length= c*angle/360
    n = int(c/4)+3
    step_length= arc_length/n
    step_angle=angle/n

    # for i in range(n):
    #     t.fd(step_length)
    #     t.lt(step_angle) 
    
    polyline(t, step_length, n, step_angle)   

def cone(t):
    t.lt(80)
    t.fd(200)
    t.rt(155)
    t.fd(200)

def draw_a(t):
    t.lt(65)
    t.fd(200)
    t.rt(135)
    t.fd(200)
    t.bk(100)
    t.rt(110)
    t.fd(80)

def draw_p(t):
    t.lt(90)
    t.fd(200)
    t.rt(90)
    t.fd(20)
    t.rt(180)
    arc(t,50,-180)
    t.bk(20)

def draw_b(t):
    draw_p(t)
    t.fd(20)
    t.rt(180)
    arc(t,50,-180)
    t.bk(20)

def draw_c(t):
    t.pu()
    t.lt(90)
    t.fd(200)
    t.rt(90)
    t.pd()
    t.bk(50)
    t.lt(180)
    arc(t,100,180)
    t.fd(50)

def draw_d(t):
    t.fd(25)
    arc(t,100,180)
    t.fd(25)
    t.goto((0.00,0.00))

def draw_f(t):
    t.lt(90)
    t.fd(200)
    t.rt(90)
    t.fd(100)
    t.bk(100)
    t.rt(90)
    t.fd(100)
    t.lt(90)
    t.fd(100)

def draw_e(t):
    draw_f(t)
    t.bk(100)
    t.rt(90)
    t.fd(100)
    t.lt(90)
    t.fd(100)

def draw_g(t):
    draw_c(t)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(50)

def draw_h(t):
    t.lt(90)
    t.fd(200)
    t.bk(100)
    t.rt(90)
    t.fd(100)
    t.lt(90)
    t.fd(100)
    t.bk(200)

def draw_i(t):
    t.fd(100)
    t.bk(50)
    t.lt(90)
    t.fd(200)
    t.rt(90)
    t.fd(50)
    t.bk(100)

def draw_j(t):
    t.pu()
    t.goto((0.00,200.0))
    t.pd()
    t.fd(100)
    t.bk(50)
    t.rt(90)
    t.fd(175)
    t.rt(180)
    arc(t,25,-180)
    t.bk(25)

def draw_k(t):
    t.lt(90)
    t.fd(200)
    t.bk(100)
    t.rt(45)
    t.fd(100)
    t.bk(100)
    t.rt(90)
    t.fd(100)

def draw_l(t):
    t.bk(100)
    t.lt(90)
    t.fd(200)

def draw_n(t):
    cone(t)
    t.lt(155)
    t.fd(200)

def draw_m(t):
    draw_n(t)
    t.rt(155)
    t.fd(200)

def draw_o(t):
    arc(t,100,360)

def draw_q(t):
    arc(t,100,360)
    t.pu()
    t.lt(90)
    t.fd(50)
    t.rt(135)
    t.pd()
    t.fd(120)

def draw_r(t):
    draw_p(t)
    t.rt(65)
    t.fd(100)

def draw_s(t):
    t.fd(100)
    arc(t, 50,180)
    t.fd(50)
    t.rt(180)
    arc(t, 50, -180)
    t.bk(100)

def draw_t(t):
    t.lt(90)
    t.fd(200)
    t.rt(90)
    t.fd(50)
    t.bk(100)

def draw_u(t):
    t.pu()
    t.lt(90)
    t.fd(100)
    t.pd()
    t.lt(180)
    t.fd(100)
    arc(t, 50, 180)
    t.fd(100)

def draw_v(t):
    t.lt(180)
    cone(t)

def draw_w(t):
    t.lt(180)
    draw_m(t)

def draw_x(t):
    t.lt(45)
    t.fd(200)
    t.bk(100)
    t.rt(90)
    t.fd(100)
    t.bk(200)

def draw_y(t):
    t.lt(90)
    t.fd(100)
    t.rt(45)
    t.fd(75)
    t.bk(75)
    t.lt(90)
    t.fd(75)

def draw_z(t):
    t.bk(200)
    t.lt(35)
    t.fd(210)
    t.lt(145)
    t.fd(200)
    
draw_z(darsh)
darsh.hideturtle()
turtle.mainloop()