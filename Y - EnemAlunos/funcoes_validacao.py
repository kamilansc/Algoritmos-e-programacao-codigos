def main():
    saida = 'A opcao digitada é inválida. Tente novamente, por favor!!'
    numero = obter_num_int_faixa('Digite um número inteiro: ', 1, 5, saida)
    print(numero)


def obter_num_int(label):
    while True:
        entrada = input(label)

        try:
            return int(entrada)
        except ValueError:
            print('Valor inválido como inteiro. Tente novamente, por favor!')


def obter_num_int_faixa(label, min:int, max:int, mensagem):
    while True:
        entrada = obter_num_int(label)

        if min <= entrada <= max:
            return entrada
        else:
            print(mensagem)


if __name__ == '__main__':
    main()