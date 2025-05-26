# Início: 25/05 - 22h02
# Fim:    25/05 - 23h18

from q01_number_utils import obter_num_int_in_faixa

def main():
    print('Primeira Data:')
    dia = obter_num_int_in_faixa('Dia: ', 1, 30)
    mes = obter_num_int_in_faixa('Mês: ', 1, 12)
    ano = obter_num_int_in_faixa('Ano: ', 1, 3000)
    
    print('\nSegunda Data:')
    dia2 = obter_num_int_in_faixa('Dia: ', 1, 30)
    mes2 = obter_num_int_in_faixa('Mês: ', 1, 12)
    ano2 = obter_num_int_in_faixa('Ano: ', 1, 3000)

    qtd_total_meses1 = ano*12 + mes + dia/30
    qtd_total_meses2 = ano2*12 + mes2 + dia2/30

    diferenca_meses = qtd_total_meses2 - qtd_total_meses1
    qtd_anos = int(diferenca_meses/12)
    qtd_meses = int(diferenca_meses%12)
    qtd_dias = int((diferenca_meses%12 - int(diferenca_meses%12))*30)

    if qtd_dias != 0 and qtd_meses != 0 and qtd_anos != 0:
        print(f'\n{qtd_anos} ano(s), {qtd_meses} mes(es) e {qtd_dias} dia(s)')

    elif qtd_anos == 0 and qtd_meses == 0:
        print(f'\n{qtd_dias} dia(s)')
    elif qtd_anos == 0 and qtd_dias == 0:
        print(f'\n{qtd_meses} mes(es)')
    elif qtd_meses == 0 and qtd_dias == 0:
        print(f'\n{qtd_anos} ano(s)')
    elif qtd_anos == 0:
        print(f'\n{qtd_meses} mes(es) e {qtd_dias} dia(s)')
    elif qtd_meses == 0:
        print(f'\n{qtd_anos} ano(s) e {qtd_dias} dia(s)')
    elif qtd_dias == 0:
        print(f'\n{qtd_anos} ano(s) e {qtd_meses} mes(es)')
main()