from funcoes_uteis_copy2 import ler_num_int


def main():
    num = ler_num_int('Número: ')

    if num > 0:
        print(f'{num} é positivo')
    elif num < 0:
        print(f'{num} é negativo')


main()