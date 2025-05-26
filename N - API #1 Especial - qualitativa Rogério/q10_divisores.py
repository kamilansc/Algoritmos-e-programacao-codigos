# Início: 25/05 20h23
# Fim:    25/05 20h42

from q01_number_utils import obter_num_int_positivo, obter_num_int_min
def main():
    numA = obter_num_int_positivo('Número A: ')
    numB = obter_num_int_min('Número B: ', 11 + numA)

    num = numA
    while num <= numB:
        qtd_divisores = 0
        divisor = 2

        while divisor < num:
            if num % divisor == 0:
                qtd_divisores += 1
            divisor += 1
        print(f'{num}: ({qtd_divisores})')
        num += 1


main()