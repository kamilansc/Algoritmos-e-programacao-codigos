# 11. Leia LimiteSuperior e LimiteInferior e escreva todos os números primos entre os limites lidos.

from funcoes_uteis import ler_num_int
import math

def main():
    lim_inferior = ler_num_int('Digite o valor do LIMITE INFERIOR: ')
    lim_superior = ler_num_int('Digite o valor do LIMITE SUPERIOR: ')

    print(f'Números primos entre {lim_inferior} e {lim_superior}: ')
    while lim_inferior >= lim_inferior and lim_inferior < lim_superior:
        if lim_inferior == 1:
            lim_inferior += 1
            continue

        elif lim_inferior == 2:
            print(lim_inferior)
            lim_inferior += 1

        else:
            eh_primo = True
            i = 2   
            while i <= int(math.sqrt(lim_inferior) + 1):
                if lim_inferior % i == 0:
                    eh_primo = False
                    break
                i += 1
            if eh_primo:
                print(lim_inferior)
            
            lim_inferior += 1           


main()