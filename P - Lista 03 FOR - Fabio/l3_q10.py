from funcoes_uteis_copy3 import ler_num_int_positivo

def main():
    limt_inferior = ler_num_int_positivo('Limite inferior: ')
    limt_superior = ler_num_int_positivo('Limite superior: ')

    for num in range(limt_inferior, limt_superior+1):
        if eh_impar(num): print(num)

    print('fim')


def eh_impar(num):
    return num % 2 != 0

main()