import math

def main():
    num_min = int(input('Digite um número inteiro mínimo: '))
    num_max = int(input('Digite um número inteiro máximo: '))

    while num_min <= num_max:
        num_eh_primo(num_min)
        num_min += 1


def num_eh_primo(num):
    contador = 2
    while contador <= int(math.sqrt(num)):
        if num % contador == 0 and contador != num:
            print(f'Número {num} não é primo')
            return
        else:
            contador += 1
    print(f'Número {num} é primo')
    return


main()