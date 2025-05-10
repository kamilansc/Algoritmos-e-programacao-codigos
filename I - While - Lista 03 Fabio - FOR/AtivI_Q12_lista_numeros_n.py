# 12. Leia N e uma lista de N números e escreva a soma e a média de todos os números da lista.

from funcoes_uteis import ler_num_racional

def main():
    qtd = ler_num_racional('Digite a quantidade de números a ser digitada: ')
    total = qtd
    somatorio = 0

    while qtd > 0:
        somatorio += ler_num_racional('Digite um número: ')
        qtd -= 1
    
    media = somatorio / total

    resultado = f'''
    > Soma do(s) {total} número(s): {somatorio}
    > Média: {media}'''

    print (resultado)


main()