from funcoes_uteis_copy3 import ler_num_int_positivo

def main():
    N = ler_num_int_positivo('Número: ')

    print(f'-- Números de 1 a {N} --')
    for i in range (1, N+1):
        print(i)


main()