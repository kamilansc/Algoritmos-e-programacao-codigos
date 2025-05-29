from ..modulos import funcoes_uteis_copy1

def main():
    num = funcoes_uteis_copy1.ler_num_int('Múmero: ')

    if num > 0:
        print(f'{num} é positivo')
    elif num < 0:
        print(f'{num} é negativo')


main()