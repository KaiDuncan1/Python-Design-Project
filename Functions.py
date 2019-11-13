#function file
import turtle
import random
bob=turtle.Turtle()
turtle.colormode(255)
def polygon(sides,distance,c):
    bob.color(c)
    for times in range(sides):
        angle=360/sides
        bob.fd(distance)
        bob.right(angle)

def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()


def star(distance,c):
    bob.color(c)
    bob.begin_fill()
    for times in range(5):
        bob.fd(distance)
        bob.right(144)
    bob.end_fill()

def explosion(distance,c):
    bob.color(c)
    bob.begin_fill()
    for times in range(8):
        bob.fd(distance)
        bob.right(135)
    bob.end_fill()

def colorsquare(distance):
    bob.width(5)
    bob.begin_fill()
    bob.color("red")
    bob.fd(distance)
    bob.right(90)
    bob.color("blue")
    bob.fd(distance)
    bob.right(90)
    bob.color("green")
    bob.fd(distance)
    bob.right(90)
    bob.color("yellow")
    bob.fd(distance)
    bob.right(90)
    bob.color("hot pink")
    bob.end_fill()


def colorsquare2(distance):
    for c in ( "red","blue","green","yellow"):
        bob.color(c)
        bob.fd(distance)
        bob.right(90)
        bob.end_fill()

def polygonfill(sides,distance,c):
    bob.color(c)
    bob.begin_fill()
    for times in range(sides):
        angle=360/sides
        bob.fd(distance)
        bob.right(angle)
    bob.end_fill()

    
