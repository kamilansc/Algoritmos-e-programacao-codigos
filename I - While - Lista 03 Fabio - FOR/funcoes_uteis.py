def ler_num_int(label):
    entrada = input(label)

    try:
        numero = int(entrada)
        return numero
    except:
        print(f'Ops! A string ("{entrada}") digitada não é válida como número inteiro. Tente novamente!')
        return ler_num_int(label)

