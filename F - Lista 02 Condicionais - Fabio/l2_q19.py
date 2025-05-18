# 19. Leia a altura (em metros) e peso (em Kg) de uma pessoa, em seguida calcule o índice de massa corpórea
# (IMC = peso / altura2). Ao final, escreva se a pessoa está com peso normal (IMC abaixo de 25), obeso
# (IMC entre 25 e 30) ou obesidade mórbida (IMC acima de 30).

from l2_q15_horas_aulas import obter_numero_racional

def main():
    altura = obter_numero_racional('Digite o valor da sua altura (em metros): ')
    peso = obter_numero_racional('Digite o valor do seu peso (em quilogramas): ')

    imc = calcular_IMC(altura, peso)

    classificacao = classificar_imc(imc)

    print(f'Seu imc é {imc:.1f} e você está na classificação "{classificacao}"')


def calcular_IMC(altura, peso):
    return peso/altura**2


def classificar_imc(imc):
    if imc < 25:
        return 'Normal'
    elif imc <= 30:
        return 'Obeso'
    elif imc > 30:
        return 'Obesidade mórbida'


main()