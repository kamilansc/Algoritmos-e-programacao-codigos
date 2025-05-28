# Existem números de 4 dígitos (entre 1000 e 9999) que obedecem à seguinte característica: se dividirmos
# o número em dois números de dois dígitos, um composto pela dezena e pela unidade, e outro pelo
# milhar e pela centena, se somarmos estes dois novos números gerando um terceiro, o quadrado deste
# terceiro número é exatamente o número original de quatro dígitos. Por exemplo:
# 2025 -> dividindo: 20 e 25 -> somando temos 45 -> 45^2 = 2025.

from l2_q29 import validar_qtd_digitos
import math

def main():
    num = validar_qtd_digitos()
    if avaliar_caracteristica(num):
        print(f' >> {num} obedece a regra!')
    else:
        print(f' >> {num} não obedece a regra!')


def avaliar_caracteristica(num):
    num1 = int(num/100)
    num2 = int(num%100)
    print (f'''
    1º número: {num1}
    2º número: {num2}
    soma = {num1 + num2}
    quadrado = {(num1 + num2)**2}''')

    return (num1 + num2)**2 == num


main()