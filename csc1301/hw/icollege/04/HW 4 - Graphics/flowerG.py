"""Turtle star

Turtle can draw intricate shapes using programs that repeat simple moves.
"""


def flower():
    import turtle
    turtle.pensize(5) 
    turtle.speed(2) 
    turtle.fillcolor("yellow") 
    turtle.begin_fill() 

    for i in range(4):
        turtle.circle(80, 50)
        turtle.circle(20, 180)
        turtle.left(180)
        turtle.circle(20, 180)
        turtle.circle(80, 50)
        turtle.left(180)
    turtle.end_fill() 

    turtle.penup()
    turtle.goto(-15, 0)
    turtle.pendown()
    turtle.circle(1)


    turtle.penup()
    turtle.goto(-10, -10)
    turtle.pendown()
    turtle.right(90)
    turtle.circle(-200, 80)



flower()


