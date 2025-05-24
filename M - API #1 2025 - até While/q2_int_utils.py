def obter_num_int(label):
    entrada = input(label)

    try:
        numero = int(entrada)
        return numero
    except ValueError:
        print('Número inválido como inteiro. Tente novamente!\n')
        return obter_num_int(label)


def obter_num_int_positivo(label):
    pass


def obter_num_int_minimo(label):
    pass


def obter_num_int_maximo(label):
    pass


def obter_num_int_in_faixa(label, minimo, maximo):
    entrada = obter_num_int(label)

    if entrada >= minimo and entrada <= maximo:
        return entrada
    else:
        print(f'O número digitado não está no intervalo estabelecido [{minimo}, {maximo}]. Tente novamente!')
        return obter_num_int_in_faixa(label, minimo, maximo)