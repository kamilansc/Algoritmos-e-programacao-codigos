'''Em uma eleição presidencial existem 3 (três) candidatos. Os votos são informados através de códigos.
Os dados utilizados para a contagem dos votos obedecem à seguinte codificação:
· 1, 2, 3 = voto para os respectivos candidatos;
· 9 = voto nulo;
· 0 = voto em branco;
Escreva um algoritmo que leia o código votado por N eleitores. Ao final, calcule e escreva:
a) total de votos para cada candidato;
b) total de votos nulos;
c) total de votos em branco;
d) quem venceu a eleição.'''

from funcoes_uteis import ler_num_int_min

def main():
    num_eleitores = ler_num_int_min('Digite a quantidade de eleitores: ', 1)
    contar_votos(num_eleitores)


def contar_votos(num_eleitores):
    contador = 1
    total_votos1 = 0
    total_votos2 = 0
    total_votos3 = 0
    total_votos_branco = 0
    total_votos_nulo = 0

    while contador <= num_eleitores:
        print('Opções de voto: 1- Candidato X | 2- Canditado Y  | 3- Candidato Z')
        print('9 == Voto nulo | 0 == Voto em branco')
        voto = ler_num_int_min('Digite o seu voto: ', 0)
        print('')
        contador += 1
#        if voto not in [1, 2, 3, 9, 0]:
#            print('Ops! Você digitou uma opção que não está cadastrada. Tente novamente!!')
        if voto == 1:
            total_votos1 += 1
        elif voto == 2:
            total_votos2 += 1
        elif voto == 3:
            total_votos3 += 1
        elif voto == 9:
            total_votos_nulo += 1
        else:
            total_votos_branco += 1
        
    calc_resultado_eleicao(total_votos1, total_votos2, total_votos3, total_votos_nulo, total_votos_branco)


def calc_resultado_eleicao(total_votos1, total_votos2, total_votos3, total_votos_nulo, total_votos_branco):
    if total_votos1 > total_votos2 and total_votos1 > total_votos3:
        vencedor = 'Candidato 1'
    elif total_votos2 > total_votos1 and total_votos2 > total_votos3:
        vencedor = 'Candidato 2'
    else:
        vencedor = 'Candidato 3'

    print('')
    print(f'''{40*'*'}
-- > RESULTADO DAS ELEIÇÕES <--
    Total de votos:
        - Candidato 1: {total_votos1}
        - Candidato 2: {total_votos2}
        - Candidato 3: {total_votos3}
    - Votos Nulos: {total_votos_nulo}
    - Votos em Branco: {total_votos_branco}
    
    VENCEDOR: {vencedor}
{40*'*'}''')


main()