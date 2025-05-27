def obter_num_float(label):
    entrada = input(label)

    try:
        numero = float(entrada)
        return numero
    except ValueError:
        print('Número inválido como decimal. Tente novamente!\n')
        return obter_num_float(label)


def obter_num_float_positivo(label):
    entrada = obter_num_float(label)

    if entrada > 0:
        return entrada
    else:
        print('Número inválido como decimal positivo. Tente novamente!\n')
        return obter_num_float_positivo(label)


def obter_num_float_minimo(label, minimo):
    entrada = obter_num_float(label)
    
    if entrada >= minimo:
        return entrada
    else:
        print('O valor digitado está abaixo do mínimo permitido. Tente novamente!')
        return obter_num_float_minimo(label, minimo)