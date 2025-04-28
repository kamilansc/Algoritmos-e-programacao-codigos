'''Exercício 4: Sistema de Notas Escolares
Desenvolva um programa que receba três notas de um aluno, calcule a média e determine sua situação com base nos critérios:
● Média >= 7.0: Aprovado
● Média entre 5.0 e 6.9: Recuperação
● Média < 5.0: Reprovado
Adicionalmente, se o aluno tiver alguma nota igual a 0.0, ele estará
automaticamente reprovado.
Conhecimentos Necessários:
● Expressões booleanas compostas (AND, OR)
● Estruturas condicionais com múltiplos critérios
● Precedência de operadores lógicos
Estrutura Sugerida:
1. Função para validar notas (entre 0 e 10)
2. Função para calcular a média
3. Função para determinar a situação do aluno
4. Função principal com interação com usuário'''

from funcoes_uteis import obter_numero_racional

def main():
    nota1 = obter_numero_racional('Digite a primeira nota: ')
    nota2 = obter_numero_racional('Digite a segunda nota: ')
    nota3 = obter_numero_racional('Digite a terceira nota: ')
   
    media = calcular_media(nota1, nota2, nota3)
    situacao = situacao_aluno(media, nota1, nota2, nota3)
    print(f'O aluno ficou com média = {media} e na situação "{situacao}"')


def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3


def situacao_aluno(media, n1, n2, n3):
    if media < 5 or (n1 == 0 or n2 == 0 or n3 == 0):
        return 'Reprovado'
    if media < 6.9:
        return 'Recuperação'
    if media >= 7:
        return 'Aprovado'


main()