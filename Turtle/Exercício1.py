#   Escreva uma função chamada square que receba um parâmetro chamado t, que é um 
# turtle. Ela deve usar o turtle para desenhar um quadrado.

import turtle
bob = turtle.Turtle()

"""def main():
    square(t)"""

def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

square(bob)
turtle.mainloop()
