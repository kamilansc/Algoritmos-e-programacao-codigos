def receber_resposta(label):
    entrada = input(label)
    return entrada

def obter_numero_exceto_zero(label):
    entrada = receber_resposta(label)

    try:
        numero = int(entrada)
        if numero != 0:
            return numero
        else:
            print('\nVocê digitou 0, valor inválido. Tente novamente.')
            return obter_numero_exceto_zero(label)
    except ValueError:
        print(f'O que você digitou ("{entrada}") não é um número válido.')
        return obter_numero_exceto_zero(label)
    

def obter_numero(label):
    entrada = receber_resposta(label)

    try:
        numero = int(entrada)
        return numero
    except ValueError:
        print(f'O que você digitou ("{entrada}") não é um número válido.')
        return obter_numero(label)
    