#  Welcome to my Simplistic World
#  File: HomeScape.py
#  Student: Suzal Regmi
#
#  Course Name: CSC 1301 HW 4, Section: 036
#
#  Date: 8th Nov 2022
#  Description of Program: Using turtle graphics to design a HomeSpace

# Importing the required libraries
from turtle import *
from random import randint

# Drawing the house and its components


def house():
    speed(0)

    # Roof
    fillcolor("brown")
    begin_fill()

    left(45)
    forward(100)
    right(90)
    forward(100)
    right(135)
    forward(140)

    end_fill()

    # remaining of house

    fillcolor("yellow")
    begin_fill()
    left(90)
    forward(140)
    left(90)
    forward(140)
    left(90)
    forward(140)

    end_fill()

    # windows and doors and stuff

    penup()
    fillcolor("white")
    goto(x=70, y=-45)
    begin_fill()
    pendown()
    circle(20)
    end_fill()
    right(270)
    forward(40)
    penup()

    goto(x=50, y=-25)
    left(90)
    pendown()
    forward(40)
    penup()

    goto(x=90, y=-90)
    pendown()
    fillcolor("blue")
    begin_fill()
    forward(50)
    left(90)
    forward(30)
    left(90)
    forward(50)
    left(90)
    forward(30)
    end_fill()

    penup()
    right(180)
    forward(10)
    right(90)
    forward(30)

    fillcolor("white")
    pendown()
    circle(2)
    penup()

# Drawing the grass outside the house


def grass():
    fillcolor("green")
    goto(x=-700, y=-880)
    pendown()
    begin_fill()
    circle(750)
    end_fill()
    penup()

# Drawing the sun


def sun():
    goto(x=-800, y=450)
    fillcolor("#FDB813")
    pendown()
    begin_fill()
    circle(300)
    end_fill()
    penup()

# Drawing another window for the house


def second_window():
    goto(x=60, y=-90)
    fillcolor("white")
    begin_fill()
    pendown()
    forward(20)
    right(90)
    forward(35)
    right(90)
    forward(20)
    right(90)
    forward(35)
    end_fill()
    penup()

# Draw flowers on the grass


def flowers():
    for _ in range(10):
        setheading(0)
        a = randint(-200, 200)
        b = randint(-400, -200)
        goto(x=a, y=b)
        pensize(3)
        pencolor("yellow")
        pendown()
        fillcolor("yellow")
        begin_fill()
        circle(5)
        end_fill()
        penup()

        goto(x=a, y=b)
        pencolor("pink")
        pendown()
        fillcolor("yellow")
        begin_fill()
        circle(8)
        end_fill()
        penup()

        goto(x=a+4, y=b-4)
        pendown()
        pencolor("black")
        right(90)
        forward(30)
        penup()

# Draw clouds on the sky


def clouds():
    setheading(0)
    goto(x=200, y=200)
    pencolor("black")
    pendown()
    fillcolor("#ADD8E6")
    begin_fill()
    forward(150)
    left(90)
    forward(20)
    for _ in range(1, 15):
        left(10)
        forward(10)

    left(220)

    for _ in range(1, 18):
        left(10)
        forward(12)

    left(200)
    for _ in range(1, 18):
        left(10)
        forward(15)

    forward(18)
    left(90)
    forward(260)
    end_fill()

# Initialize the drawing


def main():
    pensize(5)
    house()
    grass()
    sun()
    second_window()
    flowers()
    clouds()

    done()


if __name__ == "__main__":
    main()
