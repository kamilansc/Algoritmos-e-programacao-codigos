# 11. Leia quatro números (opção, num 1, num2, num3) e que escreva o valor de num1 se opção igual a 1; o valor de num2 se opção for igual a 2; e o valor de num3 se 
# opção for igual a 3. Os únicos valores possíveis para a variável opção são 1, 2 e 3.

from funcoes_uteis import obter_numero

def main():
    opcao = obter_numero('Digite uma opção (1/2/3): ')

    if opcao not in [1, 2, 3]:
        print("\nVocê digitou um valor que não é válido no sistema. Tente novamente!")
        return main()
    
    num1 = obter_numero('Digite o primeiro valor possível para a variável "opção": ')
    num2 = obter_numero('Digite o segundo valor possível para a variável "opção": ')
    num3 = obter_numero('Digite o terceiro valor possível para a variável "opção": ')

    print(f'O valor que você digitou como opção foi o "{verificar_num(opcao, num1, num2, num3)}"')
    

def verificar_num(opcao, num1, num2, num3):
    if opcao == 1:
        return num1
    elif opcao == 2:
        return num2
    elif opcao == 3:
        return num3
    

main()

