def ler_num_int(label):
    entrada = input(label)

    try:
        numero = int(entrada)
        return numero
    except:
        print('Entrada digitada inválida como inteiro. Tente novamente!')
        return ler_num_int(label)


def ler_num_float(label):
    entrada = input(label)

    try:
        numero = float(entrada)
        return numero
    except:
        print('Entrada digitada inválida como inteiro. Tente novamente!')
        return ler_num_float(label)