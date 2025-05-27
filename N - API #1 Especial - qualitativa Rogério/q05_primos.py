# Início 25/05 - 16h33

import math
# Escreva uma função que verifique todos os 
# números de N até M, escreva ao lado de cada número se é ou 
# não primo.

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
            print(primo)
            if primo: 
                print(f'{contador} é primo')
            else: 
                print(f'{contador} não é primo')
        contador += 1

eh_primo(1, 20)