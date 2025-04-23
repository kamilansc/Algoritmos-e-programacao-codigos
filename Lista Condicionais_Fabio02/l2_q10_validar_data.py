# 10. Leia uma data (dia, mês e ano), verifique e escreva se a data é ou não válida.

from funcoes_uteis import obter_numero_exceto_zero

def main():
    dia = obter_numero_exceto_zero('Digite o dia: ')
    mes = obter_numero_exceto_zero('Digite o mes em numeral: ')
    ano = obter_numero_exceto_zero('Digite o ano: ')
    validar_mes(mes, dia, ano)
    

def validar_mes(mes, dia, ano):
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if validar_dia(dia):
            if validar_ano(ano):
                pass
        else:
            print('Você digitou um valor para "DIA" inválido, tente novamente.')
            main()
        
    return print('sla, to analisando ainda')

def validar_dia(dia):
    if dia <= 30:
        return True
    return False


def validar_ano(ano):
    pass
    

main()