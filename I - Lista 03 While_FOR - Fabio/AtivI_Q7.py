# 7. Leia um número N, some todos os números inteiros entre 1 e N e escreva o resultado obtido.

from funcoes_uteis import ler_num_racional

def main():
    num = ler_num_racional('Digite um número: ')
    soma = 0
    numero = num

    while num >= 1:
        soma += num
        num -= 1
    print(f'Soma de 1 a {numero}: {soma}')


main()