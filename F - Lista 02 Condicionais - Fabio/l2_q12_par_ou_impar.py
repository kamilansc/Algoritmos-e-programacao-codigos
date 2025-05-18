# 12. Leia 1 (um) número inteiro e escreva se este número é par ou impar.

from funcoes_uteis import obter_numero_inteiro

def main():
    print('')
    numero = obter_numero_inteiro('Digite um número: ')

    if eh_par(numero):
        print(f'O número {numero} é PAR!')
    elif numero % 2 != 0:
        print(f'O número {numero} é ÍMPAR!')


def eh_par(numero):
    return numero % 2 == 0


main()