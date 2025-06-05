from funcoes_uteis import ler_num_int, ler_num_float

def main():
    maior_retorno_total = float('-inf')
    maior_taxa_retorno = float('-inf')
    qtd_imoveis = ler_num_int('Quantidade de imóveis: ')


    for imovel in range (1, qtd_imoveis + 1):
        valor_compra = ler_num_float('Valor de compra do imóvel: ')
        valor_aluguel_mensal = ler_num_float('Valor do aluguel mensal: ')
        qtd_anos_alugado = ler_num_int('Quantidade de anos que o imóvel esteve alugado: ')

        valor_total_aluguel = valor_aluguel_mensal*(qtd_anos_alugado*12)
        retorno_total = valor_total_aluguel-valor_compra
        taxa_retorno = (retorno_total/qtd_anos_alugado)/100

        print(f'''
        Retorno total: {retorno_total}
        Taxa de retorno anualizada: {taxa_retorno:.2f}%''')

        if retorno_total > maior_retorno_total:
            maior_retorno_total = retorno_total
            imovel_maior_retorno = imovel
        if taxa_retorno > maior_taxa_retorno:
            maior_taxa_retorno = taxa_retorno
            imovel_maior_taxa_retorno = imovel
        
    print(f'''
        Imóvel com maior retorno: {imovel_maior_retorno}
        Imóvel com maior taxa anual de retorno: {imovel_maior_taxa_retorno}''')


main()