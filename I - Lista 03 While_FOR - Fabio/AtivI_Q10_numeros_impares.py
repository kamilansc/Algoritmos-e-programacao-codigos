# 10. Leia LimiteSuperior e LimiteInferior e escreva todos os números ímpares entre os limites lidos.

from funcoes_uteis import ler_num_racional

def main():
    lim_inferior = ler_num_racional('Digite um valor para o LIMITE INFERIOR: ')
    lim_superior = ler_num_racional('Digite um valor para o LIMITE SUPERIOR: ')

    print(f'Números ímpares entre "{lim_inferior}" e "{lim_superior}"')
    while 0 < lim_inferior <= lim_superior:
        if lim_inferior % 2 != 0:
            print(lim_inferior)
            lim_inferior += 1
        else:
            lim_inferior += 1


main()