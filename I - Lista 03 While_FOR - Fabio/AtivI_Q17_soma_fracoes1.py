from funcoes_uteis import ler_num_int

def main():
    denominador = ler_num_int('\nDigite o valor de N(denominador): ')

    contador = 1
    numerador = 1
    soma = 0

    print('\n▼ Frações ▼')
    while contador <= denominador:
        soma += numerador/contador
        print (f'{numerador}/{contador} = {(numerador/contador):.2f}')
        contador += 1
    print(f'--> soma das frações = {soma:.2f}')


main()