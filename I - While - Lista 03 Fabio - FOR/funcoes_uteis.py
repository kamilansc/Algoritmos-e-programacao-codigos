def ler_num_int(label):
    entrada = input(label)

    try:
        numero = int(entrada)
        return numero
    except:
        print(f'Ops! A string ("{entrada}") digitada não é válida como número inteiro. Tente novamente!')
        return ler_num_int(label)


def ler_num_racional(label):
    entrada = input(label)

    try:
        numero = float(entrada)
        return numero
    except:
        print(f'Ops! A string ("{entrada}") digitada não é válida como racional. Tente novamente!')
        return ler_num_racional(label)
