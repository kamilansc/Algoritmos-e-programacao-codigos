def main():
    numerador = 1
    denominador = 1
    soma = 0

    while numerador <= 99 and denominador <= 50:
        soma += numerador/denominador
        print(f'{numerador}/{denominador} = {(numerador/denominador):.2f} \t soma atual = {soma:.2f}')
        numerador += 2
        denominador += 1
    print(f'Soma total: {soma:.2f}')


main()