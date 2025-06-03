from funcoes_uteis_copy3 import ler_num_int_positivo

def main():
    num = ler_num_int_positivo('Número: ')

    soma = 0
    sequencia = []

    for denominador in range(1, num+1, 1):
        fracao = 1/denominador
        soma += fracao
        sequencia.append(f'1/{denominador}')

    print('Frações somadas:',', '.join(sequencia))
    print(f'Resultado da soma: S = {soma:.2f}')

main()