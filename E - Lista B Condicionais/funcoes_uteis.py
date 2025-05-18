def obter_numero_inteiro(label: str):
    entrada = input(label)
    try:
        numero = int(entrada)
        return numero
    except ValueError:
        print(f'O valor "{entrada}" não é um inteiro válido. Por favor tente novamente!!')
        return obter_numero_inteiro(label)

#se eu colocar outro nome substituindo 'label' o código funciona normalmente.

"""def receber_resposta(label):
    entrada = input(label)
    return entrada"""


"""
def obter_numero_inteiro(label: str):
    entrada = input(label)
    try:
        numero = int(entrada)
        return numero
    except ValueError:
        print(f'O valor "{entrada}" não é um inteiro válido. Por favor tente novamente!!')
        obter_numero_inteiro(label)"""


def obter_numero_racional(label):
    entrada = input(label)

    try:
        numero = float(entrada)
        return numero
    except ValueError:
        print(f'O que você digitou ("{entrada}") não é um número válido.')
        return obter_numero_racional(label)
