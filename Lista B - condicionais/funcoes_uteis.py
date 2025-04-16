def obter_numero_inteiro(label: str):
    entrada = input(label)
    try:
        numero = int(entrada)
        return numero
    except ValueError:
        print(f'O valor "{entrada}" não é um inteiro válido. Por favor tente novamente!!')
        return obter_numero_inteiro(label)


"""
def obter_numero_inteiro(label: str):
    entrada = input(label)
    try:
        numero = int(entrada)
        return numero
    except ValueError:
        print(f'O valor "{entrada}" não é um inteiro válido. Por favor tente novamente!!')
        obter_numero_inteiro(label)"""