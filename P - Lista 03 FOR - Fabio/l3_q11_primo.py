from funcoes_uteis_copy3 import ler_num_int_positivo

def main():
    limt_inferior = ler_num_int_positivo('Limite inferior: ')
    limt_superior = ler_num_int_positivo('Limite superior: ')

    for num in range (limt_inferior, limt_superior + 1, 1):
        if is_prime(num):
            print(f'{num} é primo')
        else:
            print(f'{num} NÃO é primo')


def is_prime(num):
    if num < 2:
        return True

    for divisor in range(2, int((num**0.5)) + 1, 1):
        if num % divisor == 0:
            return False
    return True


main()