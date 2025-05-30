# Início 25/05 - 16h33

from q01_number_utils import obter_num_int
import math
# Escreva uma função que verifique todos os 
# números de N até M, escreva ao lado de cada número se é ou 
# não primo.

def main():
    n = obter_num_int('Número N:')
    m = obter_num_int('Número M: ')

    eh_primo(n, m)
    

def eh_primo(n: int, m: int):
    contador = n
    while contador <= m:
        if contador == 1:
            print(f'{contador} é primo')
            
        elif contador == 2:
            print(f'{contador} é primo')

        else:
            divisor = 2
            primo = True
            while divisor <= int(math.sqrt(contador)):
                if contador % divisor == 0 and contador != divisor:
                    primo = False
                    break

                divisor += 1
            if primo: 
                print(f'{contador} é primo')
            else: 
                print(f'{contador} não é primo')
        contador += 1


main()