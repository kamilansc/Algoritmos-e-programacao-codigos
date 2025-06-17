from funcoes_uteis import ler_num_int, ler_num_float

def main():
    qtd_anos = ler_num_int('Quantidade de anos para a análise: ')
    metade_qtd_anos = qtd_anos/2

    maior_temp = 0
    menor_temp = 0
    somatorio_metade1 = 0
    somatorio_metade2 = 0
    somatorio_media = 0

    for ano in range(1, qtd_anos + 1):
        temp_max_anual = ler_num_float(f'Temperatura máxima média anual {ano}: ')

        if ano <= metade_qtd_anos:
            somatorio_metade1 += temp_max_anual
        else:
            somatorio_metade2 += temp_max_anual

        somatorio_media += temp_max_anual

        if maior_temp == 0 or temp_max_anual > maior_temp:
            ano_maior_temp = ano
            maior_temp = temp_max_anual
        if menor_temp == 0 or temp_max_anual < menor_temp:
            ano_menor_temp = ano
            menor_temp = temp_max_anual
    
    media_metade1 = somatorio_metade1/metade_qtd_anos
    media_metade2 = somatorio_metade2/metade_qtd_anos

    if media_metade1 > media_metade2:
        resultado = f'Resfriamento, pois a média da 1ª metade ({media_metade1:.2f}) é maior que a média da 2ª metade ({media_metade2:.2f}).'
    elif media_metade2 > media_metade1:
        resultado = f'Aquecimento, pois a média da 2ª metade ({media_metade2:.2f}) é maior que a média da 1ª metade ({media_metade1:.2f}).'
    else:
        resultado = 'Tendência de equilíbrio, pois as médias são iguais.'
    media_geral = somatorio_media/qtd_anos

    print(f'''
    Média geral: {media_geral:.2f}
    Ano de maior média : {ano_maior_temp} (Maior média: {maior_temp})
    Ano de menor média : {ano_menor_temp} (Menor média: {menor_temp})
    Tendência: {resultado}''')


main()