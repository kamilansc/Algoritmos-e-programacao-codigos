# 18. Leia dois valores e uma das seguintes operações a serem executadas (codificadas da seguinte forma: 1 –
# Adição, 2 – Subtração, 3 – Multiplicação e 4 – Divisão). Calcule e escreva o resultado dessa operação
# sobre os dois valores lidos.

from l2_q15_horas_aulas import obter_numero_racional
from funcoes_uteis import obter_numero_inteiro

def main():
    num1 = obter_numero_racional('Digite o primeiro valor: ')
    num2 = obter_numero_racional('Digite o segundo valor: ')

    print('''
Opções de operações disponíveis: 1 - Adição; 2 - Subtração; 3 - Multiplicação e 4 - Divisão''')
    
    opcao_escolhida = verificar_opcao()
    if opcao_escolhida == 1:
        print (f'Você escolheu ADIÇÃO. Resultado: {num1} + {num2} = {num1+num2}')
    elif opcao_escolhida == 2:
        print (f'Você escolheu SUBTRAÇÃO. Resultado: {num1} - {num2} = {num1-num2}')
    elif opcao_escolhida == 3:
        print (f'Você escolheu MULTIPLICAÇÃO. Resultado: {num1} * {num2} = {num1*num2}')
    elif opcao_escolhida == 4:
        print (f'Você escolheu DIVISÃO. Resultado: {num1} / {num2} = {(num1/num2):.2f}')


def verificar_opcao():
    opcao_escolhida = obter_numero_inteiro('Digite o valor da opção selecionada: ')

    if opcao_escolhida == 1 or opcao_escolhida == 2 or opcao_escolhida == 3 or opcao_escolhida == 4:
        return opcao_escolhida
    else:
        print('O valor digitado não corresponde a nenhuma das opções cadastradas. Tente novamente!')
        return verificar_opcao()


main()