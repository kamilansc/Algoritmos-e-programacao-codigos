import turtle
import math
from Exercício1_2 import polygon

bob = turtle.Turtle()

"""def circle(t, lenght, r):
    polygon(t, lenght, r)"""

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, length, n)


circle(bob, 20, 50)
turtle.mainloop()