'''Exercício 3: Verificador de Números Primos
Crie um programa que verifica se um número é primo. Um número primo é aquele que só é divisível por 1 e por ele mesmo.
Conhecimentos Necessários:
● Funções booleanas
● Operador módulo (%)
● Estruturas condicionais
Estrutura Sugerida:
1. Função booleana para verificar se um número é primo
2. Função recursiva para obter um número válido do usuário
3. Função principal para coordenar o programa'''

from funcoes_uteis import obter_numero_inteiro
import math

def main():
    label = 'Digite um número: '
    numero = obter_numero_inteiro(label)
    eh_primo(numero)


def eh_primo(num):
    if num <= 1:
        return print(f'O número {num} não é primo')
    if num == 2:
        return print(f'O número {num} é primo')
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return print(f'O número {num} não é primo!!')
    
    return print(f'O número {num} é primo!!')

main()