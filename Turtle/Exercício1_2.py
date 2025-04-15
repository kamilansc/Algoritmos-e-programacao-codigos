import turtle
bob = turtle.Turtle()

def polygon(t, length, n: int):
    valor_angulo_externo = 360/n

    for i in range (n):
            t.fd(length)
            t.lt(valor_angulo_externo)

""" 
Forma arcaicakkk:
    t.fd(length)
    t.lt(n)
    t.fd(length)
    t.lt(n)
    t.fd(length)
    t.lt(n)
    t.fd(length)
    t.lt(n)
    t.fd(length)
    t.lt(n)"""


polygon(bob, length=70, n=7)
turtle.mainloop() 