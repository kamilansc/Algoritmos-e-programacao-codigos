# Quando em uso do Motor Elétrico não há qualquer consumo de combustível (Gasolina Comum/
# Aditivada ou Álcool).
# Já quando em Motor a combustão: o consumo de energia elétrica também será zero,

#geralmente um veículo roda entre 10 e 15 km com 1 litro de gasolina.
# abastecido com Álcool o consumo é, em média, 80% disso, ou seja, 8 a 12 km/L.

# Ou seja, uma bateria que abastece o motor, quando 100% carregada, tem N Km de autonomia, 
# em média/estimativa.

#Sobre os valores (R$) envolvidos os custos são (EXEMPLO: R$ 5,99 o litro gasolina, R$ 4,12 
# o litro do álcool), já no caso de bateria considere que o abastecimento é feito por meio 
# de pontos gratuítos

def principal ():
    distancia_percorrida = float(input("Digite a distância total da viagem a ser percorrida:"))
    valor_combustível_gasolina = float(input("Digite qual o valor do litro de gasolina: "))
    valor_combustível_alcool = float(input("Digite qual o valor do litro de álcool: "))
    percentual_motor_eletrico = int(input("Digite qual o percentual de uso, na viagem, do motor elétrico: "))

    distancia_eletrico = distancia_motor_eletrico(percentual_motor_eletrico, distancia_percorrida)
    distancia_gasolina = calcular_distancia_restante(percentual_motor_eletrico, distancia_percorrida)
    qtd_litros = calcular_litros(distancia_gasolina, 15)
    valor_combustivel = valor_total_combustivel(valor_combustível_gasolina, qtd_litros)

    print(f"""
    Você conseguirar usar o motor elétrico durante {distancia_eletrico}km;
    - Se você deseja percorrer os {distancia_gasolina}km com a gasolina, você deverá abastecer {qtd_litros} litros, o que equivalem a R${valor_combustivel:.2f}.
    - Mas se você deseja percorrer os  """)


def distancia_motor_eletrico (percentual, distancia_percorrida_total):
    distancia = (percentual/100) * distancia_percorrida_total
    return distancia


def calcular_distancia_restante (percentual, distancia_percorrida_total):
    distancia_eletrico = distancia_motor_eletrico(percentual, distancia_percorrida_total)

    distancia_restante = distancia_percorrida_total - distancia_eletrico
    return distancia_restante


# def calcular_distancia_alcool (distancia_gasolina):
    distancia = (80/100) * distancia_gasolina
    return distancia


def calcular_litros (distancia_combustivel, distancia_litro):
    qtd_litros = distancia_combustivel / distancia_litro
    return qtd_litros


def valor_total_combustivel (valor_combustivel, qtd_litros):
    valor_total_combustivel = valor_combustivel * qtd_litros
    return valor_total_combustivel
