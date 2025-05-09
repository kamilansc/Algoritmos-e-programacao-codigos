# A função integrada eval toma uma string e a avalia, usando o interpretador do Python. Por exemplo:
'''>>> eval('1 + 2 * 3')
7
>>> import math
>>> eval('math.sqrt(5)')
2.2360679774997898
>>> eval('type(math.pi)')
<class 'float'>'''
# Escreva uma função chamada eval_loop que iterativamente peça uma entrada ao usuário, a avalie usando eval e exiba o resultado.

# Ela deve continuar até que o usuário digite done; então deverá exibir o valor da última expressão avaliada.

import math

def main():
    print(f'Você digitou "done"! Resultado da última expressão avaliada: {eval_loop()}')


def eval_loop():
    ultima_entrada = None

    while True:
        entrada = input('Digite uma expressão (ou done para sair): ')
        if entrada.lower() == 'done':
            break
        try:
            resultado = eval(entrada)
            print(f'Resultado da expressão "{entrada}": {resultado}')
            ultima_entrada = resultado

        except Exception as erro:
            print(f'Ocorreu um erro: "{erro}". Tente novamente!\n')
    return 'Vazio' if ultima_entrada is None else ultima_entrada


main()