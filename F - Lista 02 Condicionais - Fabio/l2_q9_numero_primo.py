# 9. Leia 1 (um) número entre 0 e 100, verifique e escreva se o número é ou não primo.

from funcoes_uteis import obter_numero_inteiro

def main():
    label = 'Digite um número de 0 a 100: '
    numero = obter_numero_inteiro(label)
    if numero >= 0 and numero <= 100:
        if eh_primo(numero):
            print(f'O número {numero} é primo.')
        else:
            print(f'O número {numero} não é primo.')
    else:
        print('Você digitou um número fora do intervalo de 0 a 100. Tente novamente.')
        main()


def eh_primo(num):
    if num < 2:
        return False
    elif num == 2 or num == 3 or num == 5 or num == 7:
        return True
    elif num % 2 == 0:
        return False
    elif num % 3 == 0:
        return False
    elif num % 5 == 0:
        return False
    elif num % 7 == 0:
        return False
    return True # se ele não for divísivel por nenhum dos acima ele retorna true indicando que o número é primo


main()