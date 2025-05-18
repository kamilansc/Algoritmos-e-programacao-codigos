"""
Exercício 1: Verificador de Ano Bissexto
Descrição do Problema:
Crie um programa que determine se um ano é bissexto ou não. Um ano é bissexto
se for divisível por 4, exceto quando é divisível por 100 mas não por 400.

Conhecimentos Necessários:
● Expressões booleanas com múltiplas condições
● Operadores lógicos (AND, OR, NOT)
● Operador módulo (%) para verificar divisibilidade

Estrutura Sugerida:
1. Função para verificar se um ano é bissexto (retorno booleano)    CHECK
2. Função para receber entrada do usuário (com validação recursiva) CHECK
3. Função principal (main) para coordenar o programa                CHECK"""

from funcoes_uteis import obter_numero_inteiro


def main():
    # ano = int(input("Ano: "))
    ano = obter_numero_inteiro('Ano: ')

    if eh_bissexto(ano):
        print(f"O ano {ano} é bissexto!!")

    else:
        print(f"O ano {ano} NÃO é bissexto!!")


def eh_bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0


main()