def main():
    entrada = input()
    A = int(entrada.split()[0])
    B = int(entrada.split()[1])
    C = int(entrada.split()[2])
    D = int(entrada.split()[3])

    if B > C and D > A and (C+D > A+B) and (C > 0 and D > 0) and eh_par(A):
        print('Valores aceitos')
    else:
        print('Valores nao aceitos')


def eh_par(num):
    return num % 2 == 0


main()