# 3. Leia as variáveis A0, Limite e R e escreva os valores menores que Limite gerados pela Progressão
# Aritmética que tem por valor inicial A0 e razão R.

from funcoes_uteis import ler_num_racional

def main():
    a0 = ler_num_racional('Digite o valor de A0: ')
    r = ler_num_racional('Digite o valor da razão da PA: ')
    limite = ler_num_racional('Digite o valor limite da PA: ')
    print('')
    
    valor = a0

    print(f'>> Valores da PA de A0 = {a0}, r = {r} e limite = {limite} <<')
    
    if r > 0:
        while valor < limite:
            print('\t', valor)
            valor += r

    else:
        while valor > limite:
            print('\t', valor)
            valor += r


main()