def Stars(t,s,n):
    a = 360/s
    t.speed(15)
    t.width(5)
    for times in range(n):
        t.color(40+times-15,10,100+times)
        t.forward(times*4)
        t.left(a)
        t.forward(times*2)
        t.left(120)
        t.forward(times*6)
        t.left(50)

def Polygon(t,s,d):
    angle = 360/s
    for times in range(s):
        t.forward(d)
        t.left(angle)

def Cosmos(t,a,n):
    for times in range(n):
        c = 10+times,0,5+times
        t.color(c)
        Polygon(t,7,2*times)
        t.right(a)
    for times in range(80):
        c = 30+times,5,50+times
        t.color(c)
        Polygon(t,5,2*times)
        t.right(a)

def Wirl(t,s,n):
    a = 360/s
    t.speed(15)
    t.width(5)
    for times in range(n):
        t.color(50+times,80+times,150+times)
        t.forward(times*2)
        t.left(a)
        t.forward(times*1)
        t.left(100)
        t.forward(times*3)
        t.left(40)

def Wirlbend(t,s,n):
    a = 360/s
    t.speed(15)
    t.width(5)
    for times in range(n):
        t.color(100+times,20+times,150+times)
        t.forward(times*2)
        t.left(a)
        t.forward(times*1)
        t.left(100)
        t.forward(times*3)
        t.left(40)
        t.forward(times*2)
        t.left(30)

def Twirlbend(t,s,n):
    a = 360/s
    t.speed(15)
    t.width(5)
    for times in range(n):
        t.color(70+times,30+times,150+times)
        t.forward(times*2)
        t.left(a)
        t.forward(times*1)
        t.left(100)
        t.forward(times*3)
        t.left(50)
        t.forward(times*2)
        t.left(40)
