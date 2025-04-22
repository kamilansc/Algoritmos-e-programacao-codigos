from funcoes_uteis import receber_resposta

def main():
    label = 'Digite um número:'
    numero1: int = receber_resposta(label)
    numero2: int = receber_resposta(label)
    numero3: int = receber_resposta(label)


    if numero1>numero2 and numero1>numero3:
        print(f'O maior número é o {numero1}')
    elif numero2>numero1 and numero2>numero3:
        print(f'O maior número é o {numero2}')
    elif numero3>numero1 and numero3>numero2:
        print(f'O maior número é o {numero3}')
    elif numero1 == numero2 == numero3:
        print('Os números são iguais!!')

main()