def main():
    entrada = obter_num_int()
    num1 = entrada[0]
    num2 = entrada[1]
    num3 = entrada[2]

    if num1 < num2 and num1 < num3:
        if num2 < num3:
            ordem_crescente = f'{num1}\n{num2}\n{num3}'
        else:
            ordem_crescente = f'{num1}\n{num3}\n{num2}'
    elif num2 < num1 and num2 < num3:
        if num1 < num3:
            ordem_crescente = f'{num2}\n{num1}\n{num3}'
        else:
            ordem_crescente = f'{num2}\n{num3}\n{num1}'
    elif num3 < num1 and num3 < num2:
        if num1 < num2:
            ordem_crescente = f'{num3}\n{num1}\n{num2}'
        else:
            ordem_crescente = f'{num3}\n{num2}\n{num1}'
    
    print(ordem_crescente)
    print(f'\n{num1}\n{num2}\n{num3}')


def obter_num_int():
    numeros = input()

    try:
        num1 = int(numeros.split()[0])
        num2 = int(numeros.split()[1])
        num3 = int(numeros.split()[2])
        return num1, num2, num3
    except:
        return obter_num_int()


main()