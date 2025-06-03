from funcoes_uteis_copy3 import ler_num_int_positivo, ler_num_int

def main():
    n = ler_num_int_positivo('Quantidade de elementos: ')

    soma = 0
    for num in range (1, n+1):
        entrada = ler_num_int(f'Digite o {num}º número para incrementar à lista: ')
        soma += entrada

    media = soma/n
    
    print(f'''
        Somatório: {soma}
        Média: {media:.2f}''')

main()