# 14. Leia 5 (cinco) números inteiros, calcule a sua média e escreva os que são maiores que a média.

from funcoes_uteis import obter_numero_inteiro

def main():
    num1 = obter_numero_inteiro('Digite o primeiro número: ')
    num2 = obter_numero_inteiro('Digite o segundo número: ')
    num3 = obter_numero_inteiro('Digite o terceiro número: ')
    num4 = obter_numero_inteiro('Digite o quarto número: ')
    num5 = obter_numero_inteiro('Digite o quinto número: ')

    print('Média:', calcula_media(num1, num2, num3, num4, num5))
    eh_maior(calcula_media(num1, num2, num3, num4, num5), num1, num2, num3, num4, num5)


def calcula_media(num1, num2, num3, num4, num5):
    return (num1 + num2 + num3 + num4 + num5) / 5


def eh_maior(media, num1, num2, num3, num4, num5):
    if num1 > media:
        print(f'O número {num1} é maior que a média')
    if num2 > media:
        print(f'O número {num2} é maior que a média')
    if num3 > media:
        print(f'O número {num3} é maior que a média')
    if num4 > media:
        print(f'O número {num4} é maior que a média')
    if num5 > media:
        print(f'O número {num5} é maior que a média')


main()