# 15. Leia N, calcule e escreva os N primeiros termos de seqüência (1, 3, 6, 10, 15,...).

from funcoes_uteis import ler_num_int

def main():
    num = ler_num_int('Digite um número: ')

    contador = 1
    a0 = 0

    print(f'\n >> {num} Números da sequência <<')
    while num > 0:
        a0 += contador
        contador += 1
        num -= 1
        print('\t', a0)


main()