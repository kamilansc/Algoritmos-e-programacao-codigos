# 8. Leia N , LimiteSuperior e LimiteInferior e escreva todos os múltiplos de N entre os limites lidos.

from funcoes_uteis import ler_num_int

def main():
    num = ler_num_int('Digite um número para visualizar seus múltiplos: ')
    lim_superior = ler_num_int('Digite um número como LIMITE SUPERIOR: ')
    lim_inferior = ler_num_int('Digite um número como LIMITE INFERIOR: ')
    i = 0

    print(f'\nMúltiplos de {num} entre {lim_inferior} e {lim_superior}:')

    while True:
        i += 1
        multiplicacao = num * i
        if lim_superior > multiplicacao and multiplicacao >= lim_inferior:
            print(f'\t{num} x {i} = {multiplicacao} <--')
        elif multiplicacao == lim_superior:
            print(f'\t{num} x {i} = {multiplicacao} <--')
            break
        elif multiplicacao > lim_superior:
            break

main()