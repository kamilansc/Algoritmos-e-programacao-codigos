from funcoes_uteis_copy3 import ler_num_int_positivo, ler_num_int

def main():
    n = ler_num_int_positivo('Quantidade de elementos: ')

    maior_num = float('-inf')
    for num in range(1, n+1, 1):
        entrada = ler_num_int(f'Digite o {num}º número da lista: ')

        if entrada > maior_num:
            maior_num = entrada
    
    print(f'\n>> Maior número digitado: {maior_num}')


main()