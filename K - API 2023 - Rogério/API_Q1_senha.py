'''[q1_senha] Atualmente precisamos em vários momentos criar
senhas numéricas para acesso a serviços diversos. Muitos
sistemas têm políticas de senha, evitando assim senhas comuns
como por exemplo: 123456, ou 223344.
Seu objetivo portanto é fazer um Gerador de Senhas com as
seguintes regras:
- Numérica com tamanho fixo de N dígitos
- Não deve permitir que o digital atual seja igual ao anterior
- Não pode também ser antecessor ou sucessor imediato.
- O usuário vai pedir uma senha, e então você deve mostrar a
senha sugerida seguindo as regras.
- E então perguntar se ele está satisfeito com a senha
gerada. Caso negativo, gerar nova senha. Continue assim
até ele ficar satisfeito.'''

import random
from funcoes_uteis_copy1 import ler_num_int_min

def main():
    print(40*'-')
    print('   >>> S2 GERADOR DE SENHAS S2 <<<')
    qtd_digitos = ler_num_int_min('Digite o número de dígitos desejado na sua senha: ', 2)
    print(f'    {gerar_senha(qtd_digitos)}')

    entrada = input('\nVocê gostou da sua senha (S ou s - Sim / N ou n - Não)? ')
    while entrada.lower() != 's':
        print(' Ok, irei gerar uma nova senha.')
        print(f'    {gerar_senha(qtd_digitos)}')
        entrada = input('\nVocê gostou da sua senha (S ou s - Sim / N ou n - Não)? ')

    print('Que bom que gostou!!\n')
    print('''   
        Fim por fim feito por mim
                - Silva, Rogério
    
        Créditos: professor Rogério Silva''')

def gerar_senha(qtd_digitos):
    senha = ''
    dig_anterior = ''
    while len(senha) < qtd_digitos:
        dig_atual = str(random.randint(0, 9))
        if senha == '' or (dig_anterior != dig_atual and (diferenca(dig_atual, dig_anterior) not in [1, -1])) :
            dig_anterior = dig_atual
            senha = senha + dig_atual

    return f'Senha gerada: {senha}'


def diferenca(dig_atual, dig_anterior):
    diferenca = int(dig_atual) - int(dig_anterior)
    return diferenca


main()