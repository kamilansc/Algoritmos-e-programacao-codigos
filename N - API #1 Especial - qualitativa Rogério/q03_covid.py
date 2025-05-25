# Início 25/05 - 15h27
# pausa

from q1_number_utils import obter_num_int_positivo

def main():
    qtd_casos_atual = input('Quantidade de casos: ')
    somatorio = 0

    while qtd_casos_atual != 'Fim':
        try:
            qtd_casos_atual = int(qtd_casos_atual)
        except:
            print('Valor não computado')
            qtd_casos_atual = obter_num_int_positivo('Quantidade de casos: ')
        
        qtd_casos_anterior = qtd_casos_atual

        somatorio += qtd_casos_atual

        media = somatorio / qtd_casos_atual
        
        variacao = qtd_casos_anterior - 0.15*qtd_casos_anterior

        if qtd_casos_atual < variacao:
            print('Conceito: Em Estabilidade')
        else:
            print('Conceito: Em Alta')
        
        qtd_casos_anterior = qtd_casos_atual
        qtd_casos_atual = input('Quantidade de casos: ')


main()