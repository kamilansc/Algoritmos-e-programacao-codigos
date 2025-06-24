def main():
    numeros = obter_nums_int()
    num1 = numeros[0]
    num2 = numeros[1]

    if num1 % num2 == 0 or num2 % num1 == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')


def obter_nums_int():
    entrada = input().split()
    
    try:
        if len(entrada) != 2:
            raise ValueError

        return int(entrada[0]), int(entrada[1])
    except:
        return obter_nums_int()


main()