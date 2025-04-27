# 27. Determine a idade de uma pessoa, em anos, meses e dias, dadas a data (dia, mês e ano) do seu
# nascimento e a data (dia, mês e ano) atual.

def main():
    dia_atual = int(input('Informe que dia é hoje: '))
    mes_atual = int(input('Informe que mês estamos: '))
    ano_atual = int(input('Informe em que ano estamos: '))
    dia_niver = int(input('Digite o dia do seu nascimento: '))
    mes_niver = int(input('Digite o mês do seu nascimento:'))
    ano_niver = int(input('Digite o ano do seu nascimento:'))
    print(calcula_idade(dia_niver, mes_niver, ano_niver, dia_atual, mes_atual, ano_atual))


def calcula_idade(dia_niver, mes_niver, ano_niver, dia_atual, mes_atual, ano_atual):
    if mes_atual >= mes_niver:

        if dia_atual >= dia_niver:
            anos = ano_atual - ano_niver
            meses = mes_atual - mes_niver
            dias = dia_atual - dia_niver
            return anos, meses, dias

        if dia_atual < dia_niver:
            anos = (ano_atual - ano_niver) - 1
            dias = 30 - dia_atual
            meses = 12 - (mes_niver - mes_atual) - 1
            return anos, meses, dias

    elif mes_atual < mes_niver:
        anos = anos - 1

        if dia_atual > dia_niver:
            meses = 12 - (mes_niver - mes_atual)
            dias = dia_atual - dia_niver
        elif dia_atual < dia_niver:
            meses = 12 - (mes_niver - mes_atual) - 1
            dias = dia_atual

        return anos, meses, dias


main()