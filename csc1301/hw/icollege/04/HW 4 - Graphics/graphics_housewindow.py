import turtle
import math
import tkinter
count = 0
while count < 4:
    turtle.right(90)
    turtle.forward(200)
    count = count + 1

turtle.left(135)
turtle.forward(200/math.sqrt(2))
turtle.left(90)
turtle.forward(200/math.sqrt(2))
turtle.up()
turtle.left(135)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.down()

count = 0
while count < 4:
    turtle.right(90)
    turtle.forward(60)
    count = count + 1

turtle.up()
turtle.backward(30)
turtle.right(90)
turtle.down()
turtle.forward(60)

turtle.up()
turtle.backward(30)
turtle.right(90)
turtle.backward(30)
turtle.down()
turtle.forward(60)

turtle.mainloop()