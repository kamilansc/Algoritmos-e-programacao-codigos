# 13. Leia 5 (cinco) números inteiros e escreva o maior e o menor deles. Considere que todos os valores são diferentes.

from funcoes_uteis import obter_numero

def main():
    label = 'Digite um número: '
    num1 = obter_numero(label)
    num2 = obter_numero(label)

    if num_eh_diferente(label, num1, num2, 0, 0, 0):
        num3 = obter_numero(label)
# num1 != num3 and num2 != num3
        if num_eh_diferente(label, num1, num2, num3, 0 ,0):
            num4 = obter_numero(label)
            if num1 != num4 and num2 != num4 and num3 != num4:      
                num5 = obter_numero(label)
            else:
                print(f'\nO número "{num4}" já foi digitado anteriormente. Por favor digite todos os números novamente!')
                return main()
        else:
            print(f'\nO número "{num3}" já foi digitado anteriormente. Por favor digite todos os números novamente!')
            return main()
    else:
        print(f'\nO número "{num2}" já foi digitado anteriormente. Por favor digite todos os números novamente!')
        return main()


def num_eh_diferente(label, num1, num2, num3, num4, num5):
    if num1 != num2:
        num3 = obter_numero(label)
    return False


main()