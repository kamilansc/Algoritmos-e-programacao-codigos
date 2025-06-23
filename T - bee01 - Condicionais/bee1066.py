def main():
    qtd_num_par = 0
    qtd_num_impar = 0
    qtd_num_negativo = 0
    qtd_num_positivo = 0
    for num in range(1, 6):
        numero = obter_num_int()

        if eh_par(numero):
            qtd_num_par += 1
        if eh_positivo (numero):
            qtd_num_positivo += 1
        if eh_negativo (numero):
            qtd_num_negativo += 1
        if not eh_par(numero):
            qtd_num_impar += 1
    
    print(f'{qtd_num_par} valor(es) par(es)')
    print(f'{qtd_num_impar} valor(es) impar(es)')
    print(f'{qtd_num_positivo} valor(es) positivo(s)')
    print(f'{qtd_num_negativo} valor(es) negativo(s)')


def obter_num_int():
    entrada = input()

    try:
        return int(entrada)
    except:
        return obter_num_int()


def eh_par(num):
    return num % 2 == 0


def eh_positivo(num):
    return num > 0


def eh_negativo(num):
    return num < 0

main()