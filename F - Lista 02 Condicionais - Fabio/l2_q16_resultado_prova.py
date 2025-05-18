# 16. Leia duas notas de um aluno e escreva na tela a palavra “Aprovado” se a média das duas notas for maior ou igual a 7,0. 
# Caso a média seja inferior a 7,0, o programa deve ler a nota do exame e calcule a média final. Se esta média for maior ou igual 
# a 5,0, o programa deve escreva “Aprovado”, caso contrário deve escreva “Reprovado”.

from l2_q15_horas_aulas import obter_numero_racional

def main():
    nota1 = obter_numero_racional('Digite sua primeira nota: ')
    nota2 = obter_numero_racional('Digite sua segunda nota: ')

    if calcula_media_inicial(nota1, nota2) >= 7:
        print(f'Sua média é {calcula_media_inicial(nota1, nota2)}. Você foi aprovado!! ')

    elif calcula_media_inicial(nota1, nota2) < 7:
        if calcula_media_final(nota1, nota2, ler_nota_exame_final()) >= 5:
            print('Você foi aprovado no exame final!!')
        else:
            print('Você foi reprovado no exame final!!')


def calcula_media_inicial(nota1, nota2):
    return (nota1 + nota2)/2


def ler_nota_exame_final():
    return obter_numero_racional('Digite sua nota no exame final: ')


def calcula_media_final(nota1, nota2, nota_exame_final):
    return (nota1 + nota2 + nota_exame_final)/3


main()
