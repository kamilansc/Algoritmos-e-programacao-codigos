# 7. Leia 3 (três) números (cada número corresponde a um lado do triângulo), verifique e escreva se os 3 (três) números formam um triângulo (a soma de dois lados  
# não pode ser menor que o terceiro lado). Se formam, verifique se formam um triângulo equilátero (3 lados iguais), isósceles (2 lados iguais) ou escaleno (3 lados 
# diferentes). Não existe lado com tamanho 0 (zero).

from funcoes_uteis import  obter_numero_exceto_zero

def main():
    label = 'Digite o número que vai corresponder ao lado do triângulo: '
    numero1 = int(obter_numero_exceto_zero(label))
    numero2 = int(obter_numero_exceto_zero(label))
    numero3 = int(obter_numero_exceto_zero(label))

    if eh_triangulo(numero1, numero2, numero3):
        print(classifica_triangulo(numero1, numero2, numero3))
    else:
        print('\nO(s) valor(es) que você digitou não são válidos para formar um triângulo. Tente novamente!!')
        return main()


def eh_triangulo(lado_a, lado_b, lado_c):
    return (lado_a < lado_b + lado_c) and (lado_b < lado_a + lado_c) and (lado_c < lado_a + lado_b)


def classifica_triangulo(lado_a, lado_b, lado_c):
    if lado_a == lado_b and lado_a == lado_c:
        return 'Forma-se um triângulo equilátero'
    elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        return 'Forma-se um triângulo isósceles'
    elif lado_a != lado_b and lado_a != lado_c and lado_b != lado_c:
        return 'Forma-se um triângulo escaleno'


main()