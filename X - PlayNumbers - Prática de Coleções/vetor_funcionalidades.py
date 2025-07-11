from hello_map_filter_reduce import reduzir, filtrar, eh_maior, eh_menor, eh_positivo, eh_negativo, somar
from funcoes_atualizar_colecoes import *
import random


def carregar_valores_do_arquivo(colecao, nome_arquivo):
    arquivo = open(nome_arquivo)

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


def inicializar_vetor_com_valores_automaticos(colecao):
    tamanho_colecao, minimo, maximo = pedir_infos_sobre_vetor()

    for item in range(1, tamanho_colecao+1):
        novo_valor = random.randint(minimo, maximo)
        colecao.append(novo_valor)

    return colecao


def inicializar_vetor_com_valores_do_usuario(colecao):
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


def mostrar_qtd_de_itens_na_colecao(colecao):
    return len(colecao)


def mostrar_todos_os_valores_da_colecao(colecao):
    if not colecao:
        print('''
    *** Não há nenhuma coleção de valores armazenada. 
    *** Primeiramente, inicialize os valores na opção 1 do menu.''')
    
    else:
        print(f'\n\t--- Aqui estão os valores da sua coleção atual ---\n{' - '.join(str(n) for n in colecao)}')


def mostrar_maior_e_menor_valor(colecao):
    maior_valor = reduzir(colecao, eh_maior, colecao[0])
    posicao_maior_valor = colecao.index(maior_valor)

    menor_valor = reduzir(colecao, eh_menor, colecao[0])
    posicao_menor_valor = colecao.index(menor_valor)

    return maior_valor, posicao_maior_valor, menor_valor, posicao_menor_valor


def mostrar_somatorio_dos_valores(colecao):
    somatorio = reduzir(colecao, somar, 0)
    
    return somatorio


def mostrar_media_dos_valores(colecao):
    somatorio = mostrar_somatorio_dos_valores(colecao)
    media = somatorio / len(colecao)

    return media


def mostrar_valores_positivos_e_qtd(colecao):
    nova_colecao = filtrar(colecao, eh_positivo)
    quantidade_elementos = len(nova_colecao)

    return nova_colecao, quantidade_elementos


def mostrar_valores_negativos_e_qtd(colecao):
    nova_colecao = filtrar(colecao, eh_negativo)
    quantidade_elementos = len(nova_colecao)

    return nova_colecao, quantidade_elementos


def atualizar_valor_via_regra(colecao, opcao):
    if opcao == 1:
        return multiplicar_por_valor(colecao)
    elif opcao == 2:
        return elevar_por_valor(colecao)
    elif opcao == 3:
        return reduzir_valores_uma_fracao(colecao)
    elif opcao == 4:
        return substituir_valores_negativos_por_num_aleatorio(colecao)
    elif opcao == 5:
        return ordenar_valores(colecao)
    elif opcao == 6:
        return embaralhar_valores(colecao)


def adicionar_novos_valores(colecao):
    qtd_valores = int(input('Quantos valores você deseja adicionar à coleção? '))
    for item in range(qtd_valores):
        novo_valor = int(input('Digite o novo valor: '))
        colecao.append(novo_valor)
            
    resposta_usuario = int(input('Deseja adicionar mais valores? (1 - Sim | 0 - Não) '))

    while resposta_usuario == 1:
        qtd_valores = int(input('Quantos valores você deseja adicionar à coleção? '))

        for item in range(qtd_valores):
            novo_valor = int(input('Digite o novo valor: '))
            colecao.append(novo_valor)
                
        resposta_usuario = int(input('Deseja adicionar mais um valor? (1 - Sim | 0 - Não) '))
    

def remover_itens_por_valor_exato(colecao):
    valor = int(input('Digite o valor que deseja excluir da coleção: '))

    colecao = [item for item in colecao if item != valor]
    print('Valor excluído com sucesso!')
    
    return colecao


def remover_item_por_posicao(colecao):
    posicao = int(input('Digite a posição do valor que deseja excluir da coleção: '))

    del colecao[posicao]
    return


def modificar_valor_por_posicao(colecao):
    indice = int(input('Qual posição você quer modificar o valor? '))
    novo_valor = int(input('Qual o novo valor? '))

    if 0 <= indice < len(colecao):
        colecao[indice] = novo_valor
        print('Valor atualizado com sucesso!')
    else:
        print('Índice inválido!')


def salvar_dados_em_arquivo(colecao, nome_arquivo):
    arquivo = open(nome_arquivo, 'w')
    dados = (' | '.join(str(item) for item in colecao))

    arquivo.write(dados)

    print('Dados salvos!!')