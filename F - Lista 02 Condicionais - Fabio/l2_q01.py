from funcoes_uteis import receber_resposta

def main():
    numero1 = receber_resposta('Digite um número: ')
    numero2 = receber_resposta('Digite outro número: ')
    numero3 = receber_resposta('Digite outro número: ')

    if numero1 == numero2 and numero1 == numero3:
        print('Os três números são iguais.')
    elif (numero1 == numero2 and numero1 != numero3) or (numero1 == numero3 and numero1 != numero2) or (numero2 == numero3 and numero2 != numero1):
        print('Há 2 números iguais')
    elif (numero1 != numero2) and (numero1 != numero3) and (numero2 != numero3):
        print('Não há número iguais.')


main()