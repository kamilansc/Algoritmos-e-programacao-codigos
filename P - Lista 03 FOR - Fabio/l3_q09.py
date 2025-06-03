from funcoes_uteis_copy3 import ler_num_int_positivo

def main():
    limt_inferior = ler_num_int_positivo('Limite inferior: ')
    limt_superior = ler_num_int_positivo('Limite superior: ')

    print(f'-- Números PARES entre {limt_inferior} e {limt_superior} --')
    
    for num in range(limt_inferior, limt_superior+1):
        if eh_par(num):
            print(f'{num}'.rjust(15))


def eh_par(num):
    return num % 2 == 0


main()