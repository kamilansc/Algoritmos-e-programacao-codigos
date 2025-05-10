# 2. Leia N e escreva todos os números inteiros pares de 1 a N.

from funcoes_uteis import ler_num_racional

def main():
    num = ler_num_racional('Digite um número: ')
    eh_par(num)


def eh_par(num):
    contador = 2
    while contador <= num:
        if contador % 2 == 0:
            print(contador)
            contador += 1
        contador += 1


main()