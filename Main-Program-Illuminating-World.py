import turtle

bob = turtle.Turtle()
bob.width(10)
bob.speed(11)
turtle.colormode(255)
turtle.bgcolor(0,0,0)

from Function_Universe import*
from Function_Phoenix import*
#-------------------------------------------------------------------------------
Cosmos(bob,45,103)
Stars(bob,6,70)
#-------------------------------------------------------------------------------
bob.penup()
bob.goto(-200,200)
bob.pendown()

Wirl(bob,7,50)

bob.penup()
bob.goto(-200,-200)
bob.pendown()

Wirl(bob,7,50)

bob.penup()
bob.goto(200,-200)
bob.pendown()

Wirl(bob,7,50)

bob.penup()
bob.goto(200,200)
bob.pendown()

Wirl(bob,7,50)
#-------------------------------------------------------------------------------
bob.penup()
bob.goto(0,300)
bob.pendown()

Wirlbend(bob,8,50)

bob.penup()
bob.goto(300,0)
bob.pendown()

Wirlbend(bob,8,50)

bob.penup()
bob.goto(0,-300)
bob.pendown()

Wirlbend(bob,8,50)

bob.penup()
bob.goto(-300,0)
bob.pendown()

Wirlbend(bob,8,50)
#-------------------------------------------------------------------------------
bob.penup()
bob.goto(0,300)
bob.pendown()

Twirlbend(bob,8,40)

bob.penup()
bob.goto(300,0)
bob.pendown()

Twirlbend(bob,8,40)

bob.penup()
bob.goto(0,-300)
bob.pendown()

Twirlbend(bob,8,40)

bob.penup()
bob.goto(-300,0)
bob.pendown()

Twirlbend(bob,8,40)
#-------------------------------------------------------------------------------
bob.penup()
bob.goto(0,0)
bob.pendown()
bob.right(31)
#-------------------------------------------------------------------------------
Phoenix(bob)
#-------------------------------------------------------------------------------
turtle.done()
