# 13. Leia N e uma lista de N números e escreva o maior número da lista.

from funcoes_uteis import ler_num_racional, ler_num_racional

def main():
    qtd = ler_num_racional('Digite a quantidade de números a ser digitada: ')

    '''maior_numero = 0''' # em caso de n° negativo, o 0 seria o maior, dando erro
    # float (-inf) é melhor, pois, significa o infinito negativo, ele consegue ser menor que qualquer n° real

    maior_numero = float('-inf')

    while qtd > 0:
        numero = ler_num_racional('Digite um número: ')
        if numero > maior_numero: maior_numero = numero
        qtd -= 1
    
    print(f'Maior número: {maior_numero}')


main()
