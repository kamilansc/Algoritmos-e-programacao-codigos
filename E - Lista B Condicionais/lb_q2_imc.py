# Exercício 2: Calculadora de IMC com Classificação
# Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa e forneça sua classificação de acordo com a tabela:
# ● Abaixo de 18.5: Abaixo do peso ✔
# ● Entre 18.5 e 24.9: Peso normal ✔
# ● Entre 25.0 e 29.9: Sobrepeso ✔
# ● Entre 30.0 e 34.9: Obesidade grau 1
# ● Entre 35.0 e 39.9: Obesidade grau 2
# ● Acima de 40.0: Obesidade grau 3

from funcoes_uteis import obter_numero_racional

def main():
    altura = obter_numero_racional('Digite o valor da sua altura (em metros): ')
    peso = obter_numero_racional('Digite o valor do seu peso (em quilogramas): ')

    imc = calcular_IMC(altura, peso)

    classificacao = classificar_imc(imc)

    print(f'Seu imc é {imc:.1f} e você está na classificação "{classificacao}"')


def calcular_IMC(altura, peso):
    return peso/altura**2


def classificar_imc(imc):
    if imc < 18.5:
        return 'Abaixo do peso'
    elif imc <= 24.9:
        return 'Peso normal'
    elif imc <= 29.9:
        return 'Sobrepeso'
    elif imc <= 34.9:
        return 'Obesidade grau 1'
    elif imc <= 40:
        return 'Obesidade grau 2'
    elif imc > 40:
        return 'Obesidade grau 3'


main()