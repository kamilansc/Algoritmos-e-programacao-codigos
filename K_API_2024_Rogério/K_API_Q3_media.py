# A entrada será Sexo (M ou F) e Nota (número entre 1 e 10). Encerra quando sexo for diferente de M e F.

from funcoes_uteis_copy1 import ler_num_racional_min

def main():
    sexo = input('Digite o sexo do aluno (M ou F / qualquer outra letra para encerrar): ').strip().upper()
    if sexo not in ['M', 'F']:
        print('Encerrado!')
    else:
        computar_notas(sexo)


def computar_notas(sexo):
    soma_notas = 0
    menor_nota_geral = 10.1
    maior_nota_geral = 0
    contador = 0
    qtd_mulher = 0
    qtd_homem = 0
    soma_notas_mulher = 0
    soma_notas_homem = 0

    while sexo in ['M', 'F']:
        nota = ler_num_racional_min('Digite a nota do aluno (número entre 1 e 10): ', 1)
        if nota > 10:
            nota = eh_maior_q_10(nota)

        contador += 1
        soma_notas += nota

        if sexo == 'F':
            qtd_mulher += 1
            soma_notas_mulher += nota
        else:
            qtd_homem += 1
            soma_notas_homem += nota


        if nota < menor_nota_geral:
            menor_nota_geral = nota
        
        if nota > maior_nota_geral:
            maior_nota_geral = nota
        
        print('\n-> Próximo aluno')
        sexo = input('Digite o sexo do aluno (M ou F / qualquer outra letra para encerrar): ').strip().upper()

    print('Encerrado!!')

    if soma_notas_mulher != 0:
        media_notas_mulher = soma_notas_mulher / qtd_mulher
        performance_mulher = (media_notas_mulher/10)*100
    else:
        media_notas_mulher = 0
        performance_mulher = 0
    
    if soma_notas_homem != 0:
        media_notas_homem = soma_notas_homem / qtd_homem
        performance_homem = (media_notas_homem/10)*100
    else:
        media_notas_homem = 0
        performance_homem = 0

    if contador > 0:
        media_geral = soma_notas / contador
    else:
        media_geral = 0
        maior_nota_geral = 0
        menor_nota_geral = 0
    
    desempenho_geral = avaliar_desempenho(media_geral)
    desempenho_mulher = avaliar_desempenho(media_notas_mulher)
    desempenho_homem = avaliar_desempenho(media_notas_homem)

    print(f'''
        --- Dados gerais ---
        Quantidade total de alunos: {contador}
        Média geral: {media_geral:.1f}
        Menor nota: {menor_nota_geral}
        Maior nota: {maior_nota_geral}
        Desempenho: {desempenho_geral}

        --- Mulheres ---
        Quantidade: {qtd_mulher}
        Performance: {performance_mulher:.0f}%
        Desempenho: {desempenho_mulher}

        --- Homens ---
        Quantidade: {qtd_homem}
        Performance: {performance_homem:.0f}%
        Desempenho: {desempenho_homem}
''')


def eh_maior_q_10(nota):
    while nota > 10:
        print('Não é possível salvar essa nota pois ela excede o limite 10. Digite outra nota.')
        nota = ler_num_racional_min('Digite a nota do aluno (número entre 1 e 10): ', 1)
    return nota


def avaliar_desempenho(media):
    if 0 <= media <= 2:
        desempenho = 'Péssimo'
    elif media <= 4:
        desempenho = 'Ruim'
    elif media < 7:
        desempenho = 'Regular'
    elif media < 8:
        desempenho = 'Bom'
    elif media <= 10:
        desempenho = 'Excelente'
    return desempenho


main()