# 1. Leia N e escreva todos os números inteiros de 1 a N.

from funcoes_uteis import ler_num_racional

def main():
    num = ler_num_racional('Digite um número: ')
    contador = 1

    while contador <= num:
        print (contador)
        contador += 1


main()