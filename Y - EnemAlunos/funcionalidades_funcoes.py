from funcoes_validacao import obter_num_int_faixa
from fmr_funcoes import filter, reduce, somar

def rankear_resultados_pela_media(escolas, tamanho_ranking):
    top_n_escolas = []
    escolas_ordenadas = sorted(escolas, key = lambda x:x['media_objetivas'], reverse = True)

    for i in range(min(tamanho_ranking, len(escolas_ordenadas))):
        escola = escolas_ordenadas[i]
        top_n_escolas.append(escola)

    return top_n_escolas


def rankear_resultados_pela_area(escolas, tamanho_ranking, area):
    top_n_escolas = []
    escolas_ordenadas = sorted(escolas, key = lambda x:x[area], reverse=True)

    for i in range(min(tamanho_ranking, len(escolas_ordenadas))):
        escola = escolas_ordenadas[i]
        top_n_escolas.append(escola)

    return top_n_escolas


def rankear_resultados_pelo_estado(escolas, tamanho_ranking, estado):
    escolas_estado = filter(escolas, lambda x:x['uf'] == estado)

    top_n_escolas = rankear_resultados_pela_media(escolas_estado, tamanho_ranking)

    return top_n_escolas


def rankear_resultados_pela_estado_rede(escolas, tamanho_ranking, estado, rede):
    escolas_estado_rede = filter(escolas, lambda x:x['uf'] == estado and x['rede'] == rede)

    top_n_escolas = rankear_resultados_pela_media(escolas_estado_rede, tamanho_ranking)

    return top_n_escolas


def calcular_media_nacional_area(escolas, area):
    if len(escolas) != 0:
        media_nacional = reduce(escolas, lambda acumulado, escola: acumulado + escola[area], 0) / len(escolas)
    else:
        media_nacional = 0
    
    return media_nacional


# FUNÇÕES DE EXIBIÇÃO E/OU VERIFICAÇÃO
def mostrar_menu_areas():
    menu = '''| Menu de Áreas do ENEM |
    1 - Linguagens
    2 - Matemática
    3 - Ciências da Natureza
    4 - Ciências Humanas
    5 - Redação
    Escolha uma opção: '''

    saida = 'Valor inválido entre as opções cadastradas. Tente novamente!'
    escolha = obter_num_int_faixa(menu, 1, 5, saida)

    if escolha == 1:
        return 'linguagens'
    elif escolha == 2:
        return 'matematica'
    elif escolha == 3:
        return 'ciencias_natureza'
    elif escolha == 4:
        return 'humanas'
    elif escolha == 5:
        return 'redacao'


def verificar_estado():
    estados_brasil = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO",
    "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI",
    "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]

    escolha = input('Digite o UF do estado desejado (Ex.: PI, MA, CE): ').upper()
    if escolha in estados_brasil:
        return escolha
    else:
        print('Sigla de estado inválida. Tente novamente!')
        return verificar_estado()


def verificar_rede():
    mini_menu = '''| OPCÕES DE REDES DE ENSINO |
    1 - ESTADUAL
    2 - FEDERAL
    3 - MUNICIPAL
    4 - PRIVADA
-> Digite a opcão na qual deseja fazer a consulta: '''

    saida = 'Opção inválida. Tente novamente!\n'
    escolha = obter_num_int_faixa(mini_menu, 1, 4, saida)

    if escolha == 1:
        return 'Estadual'
    elif escolha == 2:
        return 'Federal'
    elif escolha == 3:
        return 'Municipal'
    elif escolha == 4:
        return 'Privada'