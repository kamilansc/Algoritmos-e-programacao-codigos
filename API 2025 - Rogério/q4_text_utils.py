def obter_texto(label):
    entrada = input(label)

    return entrada


def obter_texto_min(label, tamanho: int):
    entrada = obter_texto(label)
    if len(entrada) >= tamanho:
        return entrada
    else:
        print('Ops! A string digitada não tem a quantidade de caracteres mínima aceita. Tente novamente!')
        return obter_texto_min(label, tamanho)


def obter_texto_max(label, tamanho):
    entrada = obter_texto(label)
    if len(entrada) <= tamanho:
        return entrada
    else:
        print('Ops! A string digitada excede a quantidade de caracteres aceita. Tente novamente!')
        return obter_texto_max(label, tamanho)


def obter_texto_in_faixa(label, tamanho_min: int, tamanho_max: int):
    entrada = obter_texto(label)

    if len(entrada) >= tamanho_min and len(entrada) <= tamanho_max:
        return entrada
    else:
        print(f'Ops! A string digitada não está na faixa [{tamanho_min, tamanho_max}] de caracteres aceita. Tente novamente!')
        return obter_texto_in_faixa(label, tamanho_min, tamanho_max)