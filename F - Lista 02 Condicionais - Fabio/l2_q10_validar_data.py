# 10. Leia uma data (dia, mês e ano), verifique e escreva se a data é ou não válida.

from funcoes_uteis import obter_numero_exceto_zero

def main():
    dia = obter_numero_exceto_zero('Dia: ')
    mes = obter_numero_exceto_zero('Mês: ')
    ano = obter_numero_exceto_zero('Ano: ')
    validar_mes(mes, dia, ano)
    

def validar_mes(mes, dia, ano):
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia <= 30:

            if validar_ano(ano):
                print('Data válida!')
            else:
                print('Data inválida!')
        else:
            print('Data inválida')

    elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia <= 31:

            if validar_ano(ano):
                print('Data válida!')
            else:
                print('Data inválida!')
        
        else:
            print('Data inválida!')
            
    elif mes == 2:
        if dia == 29:
            if ano_eh_bissexto(ano):
                print('Data válida!')
            else:
                print('Data inválida!')

        elif dia <= 28:

            if validar_ano(ano):
                print('Data válida!')
            else:
                print('Data inválida!')
        
        else:
            print('Data inválida!')
    else:
        print('Data inválida!')


def validar_ano(ano):
    if ano > 0:
        return True


def ano_eh_bissexto(ano):
    return (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0)


main()