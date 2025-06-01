# Leia as variáveis A0, Limite e R e escreva os valores menores que Limite gerados pela Progressão
# Aritmética que tem por valor inicial A0 e razão R.

from funcoes_uteis_copy3 import ler_num_int

def main():
    A0 = ler_num_int('A0: ')
    limite = ler_num_int('Limite: ')
    razao = ler_num_int('Razão da progressão: ')

    for num in range(A0, limite+1, razao):
        print(num)


main()