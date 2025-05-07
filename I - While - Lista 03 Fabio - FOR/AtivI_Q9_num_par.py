# 9. Leia LimiteSuperior e LimiteInferior e escreva todos os números pares entre os limites lidos.

from funcoes_uteis import ler_num_int

def main():
    lim_inferior = ler_num_int('Digite o valor do LIMITE INFERIOR: ')
    lim_superior = ler_num_int('Digite o valor do LIMITE SUPERIOR: ')

    print(f'\nNúmeros pares de {lim_inferior} a {lim_superior}: ')
    while 0 < lim_inferior <= lim_superior:
        if lim_inferior % 2 == 0:
            print('\t', lim_inferior)
            lim_inferior += 1
        else:
            lim_inferior += 1


main()