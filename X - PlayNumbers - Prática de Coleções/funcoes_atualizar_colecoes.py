from hello_map_filter_reduce import mapear, eh_negativo
import random

def multiplicar_por_valor(colecao):
    nova_colecao = []
    valor = int(input('\nDigite o valor que você deseja multiplicar pela coleção: '))

    for item in colecao:
        nova_colecao.append(item*valor)

    print('')
    print(f'{10*'-'} Novos valores da coleção multiplicada por {valor} {10*'-'}')
    print(' | '.join(str(item) for item in nova_colecao))
    return


def elevar_por_valor(colecao):
    nova_colecao = []
    valor = int(input('\nDigite o valor que você deseja elevar toda a coleção: '))

    for item in colecao:
        nova_colecao.append(item**valor)

    print('')
    print(f'{10*'-'} Novos valores da coleção elevada por {valor} {10*'-'}')
    print(' | '.join(str(item) for item in nova_colecao))
    return


def reduzir_valores_uma_fracao(colecao):
    nova_colecao = []
    valores = mapear(input('\nDigite a fração que você deseja dividir os valores da coleção (formato aceito: n/m): ').split('/'), int)
    numerador = valores[0]
    denominador = valores[1]
    fracao = numerador/denominador
    
    for item in colecao:
        novo_item = item/fracao
        nova_colecao.append(f'{(item/fracao):.1f}')
    
    print('')
    print(f'{10*'-'} Novos valores da coleção reduzida pela fração {numerador}/{denominador} {10*'-'}')
    print(' | '.join(str(item) for item in nova_colecao))


def substituir_valores_negativos_por_num_aleatorio(colecao):
    nova_colecao = []
    faixa = input('Digite a faixa de números aleatórios (formato: início - fim): ').split('-')
    inicio = int(faixa[0])
    fim = int(faixa[1])

    for item in colecao:
        if eh_negativo(item):
            nova_colecao.append(random.randint(inicio, fim))
        else:
            nova_colecao.append(item)
    
    print('')
    print(f'{10*'-'} Novos valores da coleção com valores negativos substituídos {10*'-'}')
    print(' | '.join(str(item) for item in nova_colecao))


def ordenar_valores(colecao):
    opcao = int(input('Você deseja ordenar em qual ordem? (1 - crescente | 2 - decrescente) '))
    if opcao == 1:
        colecao.sort()
        print('')
        print(f'{10*'-'} Coleção ordenada de forma crescente {10*'-'}')
        print(' | '.join(str(item) for item in colecao))
    elif opcao == 2:
        colecao.sort(reverse = True)
        print('')
        print(f'{10*'-'} Coleção ordenada de forma decrescente {10*'-'}')
        print(' | '.join(str(item) for item in colecao))
    

def embaralhar_valores(colecao):
    random.shuffle(colecao)
    print('Coleção embaralhada com sucesso!')