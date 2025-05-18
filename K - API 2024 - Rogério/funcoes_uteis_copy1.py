import os

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


def ler_num_int_min(label, minimo):
    entrada = input(label)
    try:
        numero = int(entrada)
        if numero < minimo:
            print(f'Ops! O número é menor que o limite estabelecido {(minimo)}, tente novamente!')
            return ler_num_int_min(label, minimo)
        return numero
    except:
        print(f'Ops! A string ("{entrada}") digitada não é válida como número inteiro. Tente novamente!')
        return ler_num_int(label)
    

def ler_num_racional_min(label, minimo):
    entrada = input(label)

    try:
        numero = float(entrada)
        if numero < minimo:
            print(f'Ops! O número é menor que o limite estabelecido {(minimo)}, tente novamente!')
        return numero
    except:
        print(f'Ops! A string ("{entrada}") digitada não é válida como racional. Tente novamente!')
        return ler_num_racional_min(label, minimo)


def limpar_tela():
    os.system('cls')