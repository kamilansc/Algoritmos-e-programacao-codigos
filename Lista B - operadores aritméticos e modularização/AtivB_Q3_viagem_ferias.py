def principal ():
    distancia_percorrida = float(input("Digite a distância total da viagem a ser percorrida:"))
    valor_combustivel_gasolina = float(input("Digite qual o valor do litro de gasolina: "))
    valor_combustivel_alcool = float(input("Digite qual o valor do litro de álcool: "))
    percentual_motor_eletrico = int(input("Digite qual o percentual de uso, na viagem, do motor elétrico: "))

    distancia_eletrico = distancia_motor_eletrico(percentual_motor_eletrico, distancia_percorrida)
    distancia_gasolina = calcular_distancia_restante(percentual_motor_eletrico, distancia_percorrida)
    qtd_litros_gasolina = calcular_litros(distancia_gasolina, 15)
    valor_combustivel = valor_total_combustivel(valor_combustivel_gasolina, qtd_litros_gasolina)
    
    qtd_litros_alcool = calcular_litros(distancia_gasolina, 12)
    
    valor_combustivel_alcool = valor_total_combustivel(valor_combustivel_alcool, qtd_litros_alcool)

    print(f"""
    Você conseguirar usar o motor elétrico durante {distancia_eletrico}km;
    - Se você deseja percorrer os {distancia_gasolina}km com a gasolina, você deverá abastecer {qtd_litros_gasolina:.2f} litros, o que equivalem a R${valor_combustivel:.2f}.
    - Mas se você deseja percorrer os {distancia_gasolina:.2f}km utilizando álcool,
    voce deverá abastecer {qtd_litros_alcool:.2f} litros, que equivalem a R${valor_combustivel_alcool:.2f}. """)


def distancia_motor_eletrico (percentual, distancia_percorrida_total):
    distancia = (percentual/100) * distancia_percorrida_total
    return distancia


def calcular_distancia_restante (percentual, distancia_percorrida_total):
    distancia_eletrico = distancia_motor_eletrico(percentual, distancia_percorrida_total)

    distancia_restante = distancia_percorrida_total - distancia_eletrico
    return distancia_restante


# def calcular_distancia_alcool (distancia_gasolina):
#  distancia = (80/100) * distancia_gasolina
#    return distancia


def calcular_litros (distancia_combustivel, distancia_litro):
    qtd_litros = distancia_combustivel / distancia_litro
    return qtd_litros


def valor_total_combustivel (valor_combustivel, qtd_litros):
    valor_total = valor_combustivel * qtd_litros
    return valor_total
    
principal()