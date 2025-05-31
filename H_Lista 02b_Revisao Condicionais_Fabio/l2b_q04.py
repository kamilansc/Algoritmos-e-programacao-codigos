from funcoes_uteis_copy2 import ler_num_racional_min

def main():
    nota1 = ler_num_racional_min('Nota 1: ', 0)
    nota2 = ler_num_racional_min('Nota 2: ', 0)

    media = calc_media_aluno(nota1, nota2)
    if media == 10:
        print('Aprovado com Distinção!!')
    elif media >= 7:
        print('Aprovado!!')
    elif media < 7:
        print('Reprovado!!')


def calc_media_aluno(nota1, nota2):
    return (nota1 + nota2)/2


main()