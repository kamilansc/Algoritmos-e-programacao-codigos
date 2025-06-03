from funcoes_uteis_copy3 import ler_num_int_positivo

def main():
    print('\n~~~ SOMADOR DE FRAÇÕES ~~~')
    num = ler_num_int_positivo('Número: ')

    denominador = num + 1
    sequencia = []
    soma = 0
    for numerador in range(1, num + 1, 1):
        fracao = numerador/denominador
        soma += fracao
        denominador -= 1
        sequencia.append(f'{numerador}/{denominador}')
        
    print(f'Frações somadadas:', ', '.join(sequencia))
    print(f'Resultado da soma: S = {soma:.2f}')

main()