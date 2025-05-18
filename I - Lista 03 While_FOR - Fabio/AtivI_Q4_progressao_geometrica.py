# 4. Leia as variáveis A0, Limite e R e escreva os valores menores que Limite gerados pela Progressão
# Geométrica que tem por valor inicial A0 e razão R.

from funcoes_uteis import ler_num_racional

def main():
    print('')
    print('>>> CALCULADORA DE PROGRESSÃO GEOMÉTRICA <<<')
    a0 = ler_num_racional('Digite o valor de A0 da PG: ')
    r = ler_num_racional('Digite o valor da razão da PG: ')
    limite = ler_num_racional('Digite o valor do limite da PG: ')
    calcular_prog_geometrica(a0, r, limite)


def calcular_prog_geometrica(a0, r, limite):
    resultado = a0
    if r > 1:
        while resultado < limite:
            print(resultado)    
            resultado *= r
    else:
        while resultado > limite:
            print(resultado)
            resultado *= r


main()