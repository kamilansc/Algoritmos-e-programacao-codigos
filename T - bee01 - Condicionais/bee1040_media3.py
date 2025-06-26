def main():
    notas = list(map(float, input().split()))
    nota1, nota2, nota3, nota4 = notas

    media = (nota1*2 + nota2*3 + nota3*4 + nota4*1)/(2+3+4+1)
    
    if media >= 7:
        print(f'Media: {media:.1f}')
        print('Aluno aprovado.')

    elif media < 5:
        print(f'Media: {media:.1f}')
        print('Aluno reprovado.')

    elif media <= 6.9:
        nota_exame = float(input())
        print(f'Media: {media:.1f}')
        print('Aluno em exame.')
        print(f'Nota do exame: {nota_exame:.1f}')

        media_final = (media + nota_exame)/2
        if media_final >= 5:
            print('Aluno aprovado.')
        elif media_final <= 4.9:
            print('Aluno reprovado.')
        print(f'Media final: {media_final:.1f}')


main()