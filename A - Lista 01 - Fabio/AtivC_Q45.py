"""45. Um algoritmo para gerenciar os saques de um caixa eletrônico deve possuir algum mecanismo para
decidir o numero de notas de cada valor que deve ser disponibilizado para o cliente que realizou o
saque. Um possível critério seria o da "distribuição ótima" no sentido de que as notas de menor valor
disponíveis fossem distribuídas em número mínimo possível. Por exemplo, se a maquina só dispõe de
notas de R$ 50, de R$ 10, de R$ 5 e de R$ 1, para uma quantia solicitada de R$ 87, o algoritmo deveria
indicar uma nota de R$ 50, três notas de R$ 10, uma nota de R$ 5 e duas notas de R$ 1. Escreva um
algoritmo que receba o valor da quantia solicitada e retorne a distribuição das notas de acordo com o
critério da distribuição ótima."""

def principal():
    valor = int(input("Digite o valor: "))
    qtd_nota_50 = calcular_qtd_notas(valor, 50)
    valor_nota_50 = qtd_nota_50 * 50

    somador_notas = 0
    somador_notas = somador_notas + valor_nota_50

    qtd_nota_10 = calcular_qtd_notas(valor - somador_notas, 10)
    valor_nota_10 = qtd_nota_10 * 10

    somador_notas = somador_notas + valor_nota_10

    qtd_nota_5 = calcular_qtd_notas(valor - somador_notas, 5)
    valor_nota_5 = qtd_nota_5 * 5

    somador_notas = somador_notas + valor_nota_5

    qtd_nota_1 = calcular_qtd_notas(valor - somador_notas, 1)

    print(f"""
    Quantidade de notas de 50: {qtd_nota_50}
    Quantidade de notas de 10: {qtd_nota_10}
    Quantidade de notas de 5: {qtd_nota_5}
    Quantidade de notas de 1: {qtd_nota_1}
""")


def calcular_qtd_notas(valor, valor_nota):
    qtd_notas = valor // valor_nota
    return qtd_notas

principal()