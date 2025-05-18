# 13. Leia 5 (cinco) números inteiros e escreva o maior e o menor deles. Considere que todos os valores são diferentes.

from funcoes_uteis import obter_numero_inteiro

def main():
    label = 'Digite um número: '
    num1 = obter_numero_inteiro(label)
    num2 = obter_numero_inteiro(label)

    if num1 != num2:
        num3 = obter_numero_inteiro(label)
        if num1 != num3 and num2 != num3:
            num4 = obter_numero_inteiro(label)
            if num1 != num4 and num2 != num4 and num3 != num4:      
                num5 = obter_numero_inteiro(label)
            else:
                print(f'\nO número "{num4}" já foi digitado anteriormente. Por favor digite todos os números novamente!')
                return main()
        else:
            print(f'\nO número "{num3}" já foi digitado anteriormente. Por favor digite todos os números novamente!')
            return main()
    else:
        print(f'\nO número "{num2}" já foi digitado anteriormente. Por favor digite todos os números novamente!')
        return main()

    maior_numero = devolve_maior_numero(num1, num2, num3, num4, num5)
    print(f'\nO MAIOR número é o "{maior_numero}".')

    menor_numero = devolve_menor_numero(num1, num2, num3, num4, num5)
    print(f'\nO MENOR número é o "{menor_numero}".')


def devolve_maior_numero(num1, num2, num3, num4, num5):
    if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
        return num1
    elif num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5:
        return num2
    elif num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5:
        return num3
    elif num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5:
        return num4
    elif num5 > num1 and num5 > num2 and num5 > num3 and num5 > num4:
        return num5


def devolve_menor_numero(num1, num2, num3, num4, num5):
    if num1 < num2 and num1 < num3 and num1 < num4 and num1 < num5:
        return num1
    elif num2 < num1 and num2 < num3 and num2 < num4 and num2 < num5:
        return num2
    elif num3 < num1 and num3 < num2 and num3 < num4 and num3 < num5:
        return num3
    elif num4 < num1 and num4 < num2 and num4 < num3 and num4 < num5:
        return num4
    elif num5 < num1 and num5 < num2 and num5 < num3 and num5 < num4:
        return num5

main()