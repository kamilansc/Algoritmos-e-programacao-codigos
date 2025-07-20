def obter_num_int(label):
    while True:
        entrada = input(label)

        try:
            return int(entrada)
        except ValueError:
            print('Valor inválido como inteiro. Tente novamente, por favor!')


def obter_num_int_positivo(label):
    while True:
        entrada = obter_num_int(label)
        
        if entrada > 0:
            return entrada
        else:
            print('Número inválido como inteiro positivo. Tente novamente, por favor!')


def obter_num_int_faixa(label, min:int, max:int, mensagem):
    while True:
        entrada = obter_num_int(label)

        if min <= entrada <= max:
            return entrada
        else:
            print(mensagem)