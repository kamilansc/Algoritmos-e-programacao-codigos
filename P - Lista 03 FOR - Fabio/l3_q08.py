# Leia N , LimiteSuperior e LimiteInferior e escreva todos os múltiplos de N entre os limites lidos.

from funcoes_uteis_copy3 import ler_num_int_positivo
import math

def main():
    n = ler_num_int_positivo('Número: ')
    limt_inf = ler_num_int_positivo('Limite inferior: ')
    limt_sup = ler_num_int_positivo('Limite superior: ')

    print(f' >> MÚLTIPLOS DE {n} NO INTERVALO DE [{limt_inf}, {limt_sup}] <<')
    inicio = (limt_inf + n - 1)//n
    for i in range (inicio, limt_sup//n):
        multiplo = n * i
        if multiplo >= limt_inf and multiplo <= limt_sup:
            print(multiplo)
        elif multiplo > limt_sup:
            break


main()