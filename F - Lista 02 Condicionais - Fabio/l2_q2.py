from funcoes_uteis import receber_resposta

def main():
    numero1 = receber_resposta('Digite o primeiro número: ')
    numero2 = receber_resposta('Digite o segundo número: ')

    if numero1 > numero2:
        print (f'O maior número é o {numero1} e o menor é o {numero2}')
    elif numero1 < numero2:
        print(f'O maior número é o {numero2} e o menor é o {numero1}')
    else:
        print('Os números são iguais.')


main()