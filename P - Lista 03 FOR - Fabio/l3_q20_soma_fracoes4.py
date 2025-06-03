from funcoes_uteis_copy3 import ler_num_int_positivo

def main():
    num = ler_num_int_positivo('Número: ')

    sequencia = []
    soma = 0
    for denominador in range (1, num + 1, 1):
        fracao = 1/denominador
        if eh_par(denominador):
            sinal = '-'
            fracao = -1*(fracao)
        else:
            sinal = ''
        soma += fracao
        
        sequencia.append(f'{sinal}{1}/{denominador}')

    print('Frações somadas:', ', '.join(sequencia))
    print(f'Resultado da soma: S = {soma:.2f}')


def eh_par(num):
    return num % 2 == 0


main()