from funcoes_uteis_copy3 import ler_num_int

def main():
    N = ler_num_int('Número: ')
    
    print(f'-- Números pares de 1 a {N} --')

    for num in range(1, N+1):
        if num % 2 == 0:
            print(num)


main()