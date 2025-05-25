# Início: 25/05 - 14h50   
# Fim:    25/05 - 15h20

def obter_num_int(label):
    while True:
        entrada = input(label)

        try:
            numero = int(entrada)
            return numero
        except:
            print('Inteiro inválido! Tente novamente!')


def obter_num_int_positivo(label):
    while True:
        num = obter_num_int(label)

        if num > 0:
            return num
        else:
            print('Inválido como inteiro positivo! Tente novamente!')


def obter_num_int_negativo(label):
    while True:
        num = obter_num_int(label)

        if num <= 0:
            return num
        else:
            print('Inválido como inteiro negativo! Tente novamente!')


def obter_num_int_min(label, minimo):
    num = obter_num_int(label)

    while num < minimo:
        print('Número abaixo do limite mínimo! Tente novamente!')
        num = obter_num_int(label)
    return num


def obter_num_int_max(label, maximo):
    num = obter_num_int(label)

    while num > maximo:
        print('Número acima do limite máximo! Tente novamente!')
        num = obter_num_int(label)
    return num


def obter_num_int_in_faixa(label, minimo, maximo):
    num = obter_num_int(label)

    while num < minimo or num > maximo:
        print('Número fora da faixa definida. Tente novamente!')
        num = obter_num_int(label)
    return num