def obter_num_int(label):
    entrada = input(label)

    try:
        numero = int(entrada)
        return numero
    except ValueError:
        print('Número inválido como inteiro. Tente novamente!\n')
        return obter_num_int(label)