import turtle
bob = turtle.Turtle()

def arc(t, length, n, angle):
    arc_lenght = 2 * 3.14159 * (angle/360)
    n = int(arc_lenght / 3) + 1
    

    for i in range (n):
            t.fd(length)
            t.lt(valor_angulo_externo)

arc(bob, 20, 50, 180)
turtle.mainloop()