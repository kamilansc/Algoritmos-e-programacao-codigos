from funcoes_uteis import ler_num_int

def main():
    num = ler_num_int('\nDigite o valor de N(corresponderá ao limite do numerador e ao denominador da primeira fração): ')

    limite_numerador = num
    denominador = num
    numerador = 1
    soma = 0

    print(f'\n▼ Frações ▼')
    while numerador <= limite_numerador:
        soma += numerador/denominador
        print(f'{numerador}/{denominador} = {(numerador/denominador):.2f}')
        numerador += 1
        denominador -= 1
    print(f'-> soma das frações = {soma:.2f}')


main()