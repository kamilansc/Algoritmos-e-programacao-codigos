def main():
    denominador = 1
    soma = 0
    sequencia = []
    for numerador in range(1, 100, 2):
        fracao = numerador/denominador
        soma += fracao
        sequencia.append(f'{numerador}/{denominador}')
        denominador += 1

    print(', '.join(sequencia))


main()