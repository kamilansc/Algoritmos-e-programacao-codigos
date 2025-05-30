from funcoes_uteis_copy1 import obter_texto, ler_num_racional_positivo

def main():
    origem = obter_texto('Origem: ')
    destino = obter_texto('Destino: ')
    valor_reais_site = ler_num_racional_positivo('Valor da passagem, em R$, no site: ')
    valor_milhas = ler_num_racional_positivo('Valor da passagem, em MILHAS: ')

    valor_milhas_padrao = calc_valor_milhas_padrao(valor_milhas)
    valor_milhas_baratas = calc_valor_milhas_baratas(valor_milhas)

    percentual_milhas_padrao = (valor_milhas_padrao/valor_reais_site)*100
    percentual_milhas_baratas = (valor_milhas_baratas/valor_reais_site)*100

    print(f'''
        Valor site (R$): R$ {valor_reais_site}
        Valor em milhas padrão (R$): R$ {valor_milhas_padrao:.2f}
            > Equivale à {percentual_milhas_padrao:.1f}% do valor do site
        Valor em milhas baratas (R$): R$ {valor_milhas_baratas:.2f}
            > Equivale à {percentual_milhas_baratas:.1f}% do valor do site''')

    if valor_milhas_padrao < valor_reais_site and valor_milhas_padrao < valor_milhas_baratas:
        print(f'''
        >>> Melhor opção: Milhas padrão (R$ {valor_milhas_padrao:.2f})''')
    elif valor_milhas_baratas < valor_reais_site and valor_milhas_baratas < valor_milhas_padrao:
        print(f'''
        >>> Melhor opção: Milhas baratas (R$ {valor_milhas_baratas:.2f})''')
    elif valor_reais_site < valor_milhas_baratas and valor_reais_site < valor_milhas_padrao:
        print(f'''
        >>> Melhor opção: Comprar pelo site em reais (R$ {valor_reais_site:.2f})''')
    else:
        print('''
        >>> As opções têm valores equivalentes ou não há uma vantagem clara.''')


def calc_valor_milhas_padrao(valor_milhas):
    valor_unidade = 70/1000
    return valor_unidade*valor_milhas


def calc_valor_milhas_baratas(valor_milhas):
    valor_unidade = 14.5/1000
    return valor_unidade*valor_milhas


main()