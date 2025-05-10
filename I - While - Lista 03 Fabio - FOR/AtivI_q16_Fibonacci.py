# 16. Leia um número N, calcule e escreva os N primeiros termos de seqüência de Fibonacci
# (0,1,1,2,3,5,8,...). O valor lido para N sempre será maior ou igual a 2.

from funcoes_uteis import ler_num_int


def main():
    num = validar_num()
    sequencia_fibonacci(num)


def validar_num():
    num = ler_num_int('Digite um número: ')
    while True:
        if num >= 2:
            return num
        else:
            num = ler_num_int('''\nO número digitado é menor que 2. Tente novamente!! 
Digite um número (a partir de 2): ''')


def sequencia_fibonacci(num):
    penultimo = 0
    ultimo = 1

    while num > 0:
        resultado = penultimo + ultimo
        ultimo = resultado
        num -= 1
        print(resultado)
'''    if num == 2:
        print(a0)
        print(a1)'''


        

main()