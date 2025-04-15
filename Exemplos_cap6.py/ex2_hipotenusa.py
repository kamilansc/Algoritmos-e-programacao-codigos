import math

def hypotenuse(cateto_a, cateto_b):
    a = cateto_a**2
    b = cateto_b**2
    sum_catetos = a + b
    c = math.sqrt(sum_catetos)
    
    return c

print("A hipotenusa é: ", hypotenuse(3, 4))