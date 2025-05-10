# 5. Leia um número, calcule e escreva seu fatorial.

from funcoes_uteis import ler_num_racional

def main():
    num = ler_num_racional('Digite um número: ')
    i = num
    numero = num #pra eu conseguir printar na linha 17

    if i == 1:
        print('Fatorial de 1: 1')

    while i > 1:
        i -= 1
        multiplicacao = num * i
        num = multiplicacao
    print(f'Fatorial de {numero}:', multiplicacao)


main()
