def obter_num_int(label):
    entrada = input(label)

    try:
        numero = int(entrada)
        return numero
    except:
        print('O que você digitou não é válido como número inteiro. Tente novamente!')
        return obter_num_int

