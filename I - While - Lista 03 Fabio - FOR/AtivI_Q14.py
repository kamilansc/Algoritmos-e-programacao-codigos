# Leia N, calcule e escreva o maior quadrado menor ou igual a N. Por exemplo, se N for igual a 38, o
# maior quadrado menor que 38 é 36 (quadrado de 6).

from funcoes_uteis import ler_num_int
# from math import isqrt


def main():
    num = ler_num_int('Digite um número: ')
    calcular_quadrado(num)


def calcular_quadrado(num):
    contador = 0
    quadrado = 0
    ultimo_valido = 0
    ultimo_contador = 0

    while quadrado <= num:
#       raiz = isqrt(num)
        ultimo_valido = quadrado
        ultimo_contador = contador-1
        quadrado = contador**2
        contador += 1
    print(f'O maior quadrado menor ou igual a {num} é: {ultimo_valido} ({ultimo_contador} x {ultimo_contador})')
#   print(f'O maior quadrado menor ou igual a {num} é: {quadrado} ({raiz} x {raiz})')


main()