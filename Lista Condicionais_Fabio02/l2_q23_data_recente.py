'''23. Leia 2 datas (cada data é composta por 3 variáveis inteiras: dia, mês e ano) e escreva qual delas é a mais
recente.'''

from funcoes_uteis import obter_numero_inteiro

def main():
    print('---- Primeira data ----')
    dia1 = obter_numero_inteiro('Digite o dia: ')
    mes1 = obter_numero_inteiro('Digite o mes: ')
    ano1 = obter_numero_inteiro('Digite o ano: ')
    print('\n---- Segunda data ----')
    dia2 = obter_numero_inteiro('Digite o dia: ')
    mes2 = obter_numero_inteiro('Digite o mes: ')
    ano2 = obter_numero_inteiro('Digite o ano: ')

    data_mais_recente = identificar_dt_recente(dia1, mes1, ano1, dia2, mes2, ano2)
    print('Data mais recente:', data_mais_recente)

def identificar_dt_recente(dia1, mes1, ano1, dia2, mes2, ano2):
    if ano1 > ano2:
        return f'{dia1}/{mes1}/{ano1}'
    elif ano2 > ano1:
        return f'{dia2}/{mes2}/{ano2}'
    elif ano1 == ano2:
        if mes1 > mes2:
            return f'{dia1}/{mes1}/{ano1}'
        elif mes2 > mes1:
            return f'{dia2}/{mes2}/{ano2}'
        elif mes1 == mes2:
            if dia1 > dia2:
                return f'{dia1}/{mes1}/{ano1}'
            elif dia2 > dia1:
                return f'{dia2}/{mes2}/{ano2}'
            elif dia1 == dia2:
                return f'{dia1}/{mes1}/{ano1} e {dia2}/{mes2}/{ano2}' 
       

main()

