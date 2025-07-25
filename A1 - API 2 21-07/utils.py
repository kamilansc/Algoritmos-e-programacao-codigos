def obter_num_inteiro(label):
    entrada = input(label)

    try:
        return int(entrada)
    
    except ValueError:
        print('Entrada inválida como inteiro.')
        return obter_num_inteiro(label)


def obter_num_float(label):
    entrada = input(label)

    try:
        return int(entrada)
    except:
        print('Entrada inválida como racional.')
        return obter_num_float(label)