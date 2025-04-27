# 17. (Leia valores inteiros em duas variáveis distintas)✔ e 
# se o resto da divisão da primeira pela segunda for 1 escreva a soma dessas variáveis mais o resto da divisão; ✔
# se for 2 escreva se o primeiro e o segundo valor são pares ou ímpares; ✔
# se for igual a 3 multiplique a soma dos valores lidos pelo primeiro; ✔
# se for igual a 4 divida a soma dos números lidos pelo segundo, se este for diferente de zero.
# Em qualquer outra situação escreva o quadrado dos números lidos.

from funcoes_uteis import obter_numero_inteiro

def main():
    valor1 = obter_numero_inteiro('Digite o primeiro valor: ')
    valor2 = obter_numero_inteiro('Digite o segundo valor: ')

    if devolve_resto_divisao(valor1, valor2) == 1:
        print(f'\nSoma dos valores: {devolve_soma(valor1, valor2)}; resto da divisão: 1')

    elif devolve_resto_divisao(valor1, valor2) == 2:
        print(eh_par_ou_impar(valor1, valor2))

    elif devolve_resto_divisao(valor1, valor2) == 3:
        print(f'''\nSomas dos valores lidos: {devolve_soma(valor1, valor2)}
Multiplicação da soma pelo valor "{valor1}": {devolve_soma(valor1, valor2) * valor1}''')
        
    elif devolve_resto_divisao(valor1, valor2) == 4 and valor2 != 0:
        print(f'''\nSoma dos valores lidos: {devolve_soma(valor1, valor2)}
Divisão da soma pelo valor "{valor2}": {(devolve_soma(valor1, valor2) / valor2):.2f}''')
        
    else:
        print(f'''\nQuadrado do valor 1: {valor1**2}
Quadrado do valor 2: {valor2**2}''')


def devolve_resto_divisao(valor1, valor2):
    return valor1 % valor2


def devolve_soma(valor1, valor2):
    return valor1 + valor2


def eh_par_ou_impar(valor1, valor2):
    if valor1 % 2 == 0 and valor2 % 2 == 0:
        return f'Os valores {valor1} e {valor2} são pares'
    elif valor1 % 2 != 0 and valor2 % 2 != 0:
        return f'Os valores {valor1} e {valor2} são ímpares'
    elif valor1 % 2 == 0 and valor2 % 2 != 0:
        return f'O valor {valor1} é par e o valor {valor2} é ímpar'
    elif valor1 % 2 != 0 and valor2 % 2 == 0:
        return f'O valor {valor1} é ímpar e o valor {valor2} é par'
    

main()