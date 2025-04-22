# 8. Leia data atual (dia, mês e ano) e data de nascimento (dia, mês e ano) de uma pessoa, calcule e escreva sua idade exata (em anos).

def main():
    dia_atual = int(input('Informe que dia é hoje: '))
    mes_atual = int(input('Informe que mês estamos: '))
    ano_atual = int(input('Informe em que ano estamos: '))
    dia_niver = int(input('Digite o dia do seu nascimento: '))
    mes_niver = int(input('Digite o mês do seu nascimento:'))
    ano_niver = int(input('Digite o ano do seu nascimento:'))
    calcula_idade(dia_niver, mes_niver, ano_niver, dia_atual, mes_atual, ano_atual)


def calcula_idade(dia_niver, mes_niver, ano_niver, dia_atual, mes_atual, ano_atual):
    idade = ano_atual - ano_niver
    if mes_atual < mes_niver:
        idade = idade - 1
        print(f'Você tem {idade} anos mas vai fazer mais um aninho esse ano no dia {dia_niver}/{mes_niver}')
    elif mes_atual == mes_niver:
        if dia_atual < dia_niver:
            print(f'Eitaaa, estamos no mês do seu aniversário!! você tem {idade-1} anos mas no dia {dia_niver}/{mes_niver} você completará {idade} anos!!')
        elif dia_atual == dia_niver:
            print(f'Que legalll, hoje é o dia do seu aniversário!! Você está completando {idade} anos. Meus parabéns!!!')
        elif dia_atual > dia_niver:
            print(f'Hmm, você completou esse mês {idade} anos.')
    elif mes_atual > mes_niver:
        print(f'Você completou no dia {dia_niver}/{mes_niver} {idade} anos.')


main()
