import random
from hello_map_filter_reduce import mapear

def main():
    menu = '''\n\tManipulação de Coleção (Vetores)
    1 - Inicializar Vetor Numérico
    0 - Sair
    Opção: '''

    opcao = int(input(menu))

    while opcao != 0:
        if opcao == 1:
            tipo_colecao = int(input('''
>>> Inicializar Vetor Numérico
    1 - Gerar valores automaticamente
    2 - Informar valores
    3 - Carregar valores de um arquivo
    Opção: '''))

            if tipo_colecao == 1:
                tamanho_colecao = int(input('Qtd valores: '))
                minimo = int(input('Valor mínimo: '))
                maximo = int(input('Valor máximo: '))

                colecao = []
                for item in range(1, tamanho_colecao+1):
                    novo_valor = random.randint(minimo, maximo)
                    colecao.append(novo_valor)
                
                opcao = int(input(menu))

            elif tipo_colecao == 2:
                tamanho_colecao = int(input('Qtd valores: '))
                minimo = int(input('Valor mínimo: '))
                maximo = int(input('Valor máximo: '))

                colecao = mapear(input('Digite os valores: ').split(), int)

                opcao = int(input(menu))

            elif tipo_colecao == 3:
                nome_arquivo = input('Nome do arquivo: ')
                colecao = carregar_valores_do_arquivo(nome_arquivo)

                print(colecao)


def carregar_valores_do_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo)
    colecao = []

    for linha in arquivo:
        valores = linha.strip().split()
        for item in valores:
            colecao.append(item)
    
    return colecao


main()