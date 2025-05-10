from funcoes_uteis import ler_num_int

def main():
    num = ler_num_int('\nDigite o valor de N: ')
    print(retorna_primo(num))

    limite_numerador = num
    numerador = 1
    limite_denominador = num
    denominador = 2

    while numerador <= limite_numerador:
        resultado = numerador/limite_denominador - (limite_numerador-numerador)/denominador
        numerador += 1
#        resultado += n


def retorna_primo(n):
    contador = 1

    while contador <= n:
        if contador % 2 == 0:
            contador += 1
        break
    return contador


main()