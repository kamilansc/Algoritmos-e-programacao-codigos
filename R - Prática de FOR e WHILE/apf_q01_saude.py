from funcoes_uteis import ler_num_int

def main():
    qtd_dias = ler_num_int('Quantidade de dias para análise: ')
    lmt_diario_clr = float(input('Limite diário de caloria: '))

    clr_diaria = 0
    menor_consumo = 0
    maior_consumo = 0
    total_caloria_periodo = 0
    dia_menor_consumo = 0
    dia_maior_consumo = 0

    for dia in range (1, qtd_dias+1):
        clr_diaria = 0
        print(f'\n>> DIA {dia}')
    
        for refeicao in range(1, 4+1):
            qtd_caloria = float(input(f'Quantidade de calorias na sua {refeicao}º refeição: '))
            clr_diaria += qtd_caloria
        
        total_caloria_periodo += clr_diaria

        
        if menor_consumo == 0 or clr_diaria < menor_consumo:
            menor_consumo = clr_diaria
            dia_menor_consumo = dia
    
        if maior_consumo == 0 or clr_diaria > maior_consumo:
            maior_consumo = clr_diaria
            dia_maior_consumo = dia
        
    media_calorica_prd = calc_media_calorica(total_caloria_periodo, qtd_dias)
    
    if media_calorica_prd > lmt_diario_clr:
        mensagem = f'Você excedeu o limite diário de {lmt_diario_clr} calorias.'
    else:
        mensagem = f'Você não excedeu o limite diário de {lmt_diario_clr} calorias.'

    print(f'''
    Média calorica diária: {media_calorica_prd:.2f} cal
    Dia com menor consumo: {dia_menor_consumo}
    Dia com maior consumo: {dia_maior_consumo}
    Situação de calorias diárias: {mensagem}''')


def calc_media_calorica(qtd_caloria, qtd_dias):
    return qtd_caloria/qtd_dias


main()