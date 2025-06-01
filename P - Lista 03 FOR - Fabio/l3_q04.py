# Leia as variáveis A0, Limite e R e escreva os valores menores que Limite gerados pela Progressão
# Geométrica que tem por valor inicial A0 e razão R.

from funcoes_uteis_copy3 import ler_num_int

def main():
    A0 = ler_num_int('A0: ')
    limite = ler_num_int('Limite: ')
    razao = ler_num_int('Razão da progressão: ')
    validar_entrada(razao)

    num = A0
    for i in range (1, 1000):
        if num >= limite:
            break
        print(f'{num}'.rjust(2))
        num *= razao


def validar_entrada (razao):
    if razao == 0:
        print('Não é válido razão = 0, tente novamente!')
        razao = ler_num_int('Razão da progressão: ')
        return validar_entrada(razao)
    return razao


main()