# 15. Leia a quantidade de horas aula dadas por dois professores e o valor por hora recebido por cada um. Escreva na tela qual dos professores tem salário total 
# maior.
from funcoes_uteis import receber_resposta

def main():
    qtd_horas1 = obter_numero_racional('Digite a quantidade de horas de aulas dada pelo professor 1: ')
    valor_hora1 = obter_numero_racional('Digite quanto esse professor ganha por hora: ')
    qtd_horas2 = obter_numero_racional('Digite a quantidade de horas de aulas dada pelo professor 2: ')
    valor_hora2 = obter_numero_racional('Digite quanto esse segundo professor ganha por hora: ')
    
    salario_prof1 = calcular_salario_total(qtd_horas1, valor_hora1)
    salario_prof2 = calcular_salario_total(qtd_horas2, valor_hora2)
    if salario_prof1 > salario_prof2:
        print(f'\nO professor 1 recebe R${salario_prof1} e tem o salário maior que o professor 2, que recebe R${salario_prof2}')
    elif salario_prof2 > salario_prof1:
        print(f'\nO professor 2 recebe R${salario_prof2} e tem o salário maior que o professor 1, que recebe R${salario_prof1}')


def calcular_salario_total(qtd_horas, valor_hora):
    return qtd_horas*valor_hora

def obter_numero_racional(label):
    entrada = receber_resposta(label)

    try:
        numero = float(entrada)
        return numero
    except ValueError:
        print(f'O que você digitou ("{entrada}") não é um número válido.')
        return obter_numero_racional(label)


if __name__ == '__main__':
    main()