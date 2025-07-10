import random
from hello_map_filter_reduce import mapear

def main():
    menu = '''\n\t>>> Bem vindo ao PlayNumbers !!! <<<
    1 - Inicializar Colecão Numérica
    2 - Mostrar todos os valores
    3 - Resetar coleção
    4 - Mostrar quantidade de itens na coleção
    
    0 - Sair
    Opção: '''

    opcao = int(input(menu))

    while opcao != 0:
        if opcao == 1:
            tipo_colecao = int(input('''
>>> Escolha como você deseja gerar o conjunto de valores:
    1 - Gerar valores automaticamente
    2 - Informar valores
    3 - Carregar valores de um arquivo
    Opção: '''))
            print('')

            if tipo_colecao == 1:
                colecao = inicializar_vetor_com_valores_automaticos()
                
            elif tipo_colecao == 2:
                colecao = inicializar_vetor_com_valores_do_usuario()

            elif tipo_colecao == 3:
                nome_arquivo = input('Qual o nome do arquivo (adicione .txt ao final)? ')
                colecao = carregar_valores_do_arquivo(nome_arquivo)

        if opcao == 2:
            try:
                print(f'\n\t--- Aqui estão os valores da sua coleção atual ---\n{' - '.join(str(n) for n in colecao)}')

            except UnboundLocalError:
                print('''
    *** Não há nenhuma coleção de valores armazenada. 
    *** Primeiramente, inicialize os valores na opção 1 do menu.''')

        if opcao == 3:
            try:
                valor_padrao = int(input('Digite um valor para substituir todos os atuais valores: '))
                colecao = resetar_valores_da_colecao(colecao, valor_padrao)
                print('>>> Sua coleção foi resetada com sucesso!! <<<')

            except UnboundLocalError:
                print('''
    *** Não há nenhuma coleção de valores armazenada. 
    *** Primeiramente, inicialize os valores na opção 1 do menu.''')
        

        opcao = int(input(menu ))


def carregar_valores_do_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo)
    colecao = []

    for linha in arquivo:
        valores = linha.strip().split()
        for item in valores:
            colecao.append(item)
    
    return colecao


def pedir_infos_sobre_vetor():
    print('>>> Digite, a seguir, algumas informações sobre o vetor.')
    tamanho_colecao = int(input('Qtd valores: '))
    minimo = int(input('Valor mínimo: '))
    maximo = int(input('Valor máximo: '))

    return tamanho_colecao, minimo, maximo


def inicializar_vetor_com_valores_automaticos():
    colecao = []
    tamanho_colecao, minimo, maximo = pedir_infos_sobre_vetor()

    for item in range(1, tamanho_colecao+1):
        novo_valor = random.randint(minimo, maximo)
        colecao.append(novo_valor)

    return colecao


def inicializar_vetor_com_valores_do_usuario():
    colecao = []
    tamanho_colecao, minimo, maximo = pedir_infos_sobre_vetor()

    for posicao in range(1, tamanho_colecao+1):
        novo_valor = int(input(f'>>> Digite o {posicao}° valor: '))
        
        while novo_valor < minimo or novo_valor > maximo:
            print('Valor inválido, por favor, tente novamente!\n')
            novo_valor = int(input(f'>>> Digite o {posicao}° valor: '))
   
        colecao.append(novo_valor)

    return colecao


def resetar_valores_da_colecao(colecao, valor_padrao):
    colecao = [valor_padrao for item in colecao]

    return colecao
    # nova_colecao = []
    # for item in colecao:
        # nova_colecao.append(valor_padrao)
    # colecao = nova_colecao


main()