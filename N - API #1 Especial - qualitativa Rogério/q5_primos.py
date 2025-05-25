# Início 25/05 - 16h33

import math
# Escreva uma função que verifique todos os 
# números de N até M, escreva ao lado de cada número se é ou 
# não primo.

def eh_primo(n: int, m: int):
    contador = n
    while contador <= m:
        divisor = 2
        primo = True
        while divisor < math.sqrt(contador):
            if contador % divisor == 0 and contador != divisor:
                primo = False
                divisor += 1
            else:
                divisor += 1
        if primo: 
            print(f'{contador} é primo')
        else: 
            print(f'{contador} não é primo')
        contador += 1

eh_primo(1, 20)