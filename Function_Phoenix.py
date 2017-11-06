def Phoenix(bob):
    bob.color(255,100,100)       
    #---------------------------------------------------------------------------
    bob.penup()
    bob.goto(100,40)
    bob.pendown()
    #---------------------------------------------------------------------------
    for times in range(20):
        bob.forward(1+times)
        bob.left(3)
    
    bob.right(125)

    for times in range(20):
        bob.forward(3+times)
        bob.right(4)

    bob.left(125)

    for times in range(17):
        bob.forward(1+times)
        bob.left(3)

    bob.right(125)

    for times in range(17):
        bob.forward(3+times)
        bob.right(4)

    bob.left(125)

    for times in range(14):
        bob.forward(1+times)
        bob.left(3)

    bob.right(125)

    for times in range(14):
        bob.forward(3+times)
        bob.right(3)
        bob.forward(1+times)
        bob.right(3)

    #----------------------------------------------------------------------------
    bob.penup()
    bob.goto(-100,40)
    bob.pendown()
    bob.right(335)
    #----------------------------------------------------------------------------

    for times in range(20):
        bob.forward(1+times)
        bob.right(3)

    bob.left(125)

    for times in range(20):
        bob.forward(3+times)
        bob.left(4)

    bob.right(125)

    for times in range(17):
        bob.forward(1+times)
        bob.right(3)

    bob.left(125)

    for times in range(17):
        bob.forward(3+times)
        bob.left(4)

    bob.right(125)

    for times in range(14):
        bob.forward(1+times)
        bob.right(3)

    bob.left(125)

    for times in range(14):
        bob.forward(3+times)
        bob.left(3)
        bob.forward(1+times)
        bob.left(3)

    #----------------------------------------------------------------------------
    bob.penup()
    bob.goto(-85,80)
    bob.pendown()
    bob.left(360)
    #----------------------------------------------------------------------------

    for times in range(12):
        distance=2
        bob.forward(1+distance)
        bob.right(6)
        bob.forward(5)

    for times in range(6):
        distance=1
        bob.forward(1+distance)
        bob.left(10)
        bob.forward(10)

    bob.right(90)

    for times in range(5):
        distance=2
        bob.forward(1+distance)
        bob.right(10)
        bob.forward(1)
        
    #----------------------------------------------------------------------------
    bob.penup()
    bob.goto(-85,80)
    bob.pendown()
    bob.right(275)
    #----------------------------------------------------------------------------

    for times in range(12):
        distance=5
        bob.forward(1+distance)
        bob.right(6)
        bob.forward(7)

    for times in range(6):
        distance=1
        bob.forward(1+distance)
        bob.left(10)
        bob.forward(20)
        
    #----------------------------------------------------------------------------
    bob.penup()
    bob.goto(60,-10)
    bob.pendown()
    bob.right(2)
    #----------------------------------------------------------------------------

    for times in range(12):
        distance=5
        bob.forward(1+distance)
        bob.right(6)
        bob.forward(10)
        
    #----------------------------------------------------------------------------
    bob.penup()
    bob.goto(-25,-200)
    bob.pendown()
    bob.left(30)
    #----------------------------------------------------------------------------

    for times in range(12):
        distance=5
        bob.forward(1+distance)
        bob.right(4)
        bob.forward(10)
        
    #----------------------------------------------------------------------------
    bob.penup()
    bob.goto(10,-200)
    bob.pendown()
    bob.left(70)
    #----------------------------------------------------------------------------

    for times in range(12):
        distance=6
        bob.forward(1+distance)
        bob.right(3)
        bob.forward(10)
        
    #----------------------------------------------------------------------------
    bob.penup()
    bob.goto(40,-200)
    bob.pendown()
    bob.left(40)
    #----------------------------------------------------------------------------

    for times in range(12):
        distance=5
        bob.forward(1+distance)
        bob.left(3)
        bob.forward(10)
