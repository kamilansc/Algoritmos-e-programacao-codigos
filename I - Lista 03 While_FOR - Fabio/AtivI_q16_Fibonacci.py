# 16. Leia um número N, calcule e escreva os N primeiros termos de seqüência de Fibonacci
# (0,1,1,2,3,5,8,...). O valor lido para N sempre será maior ou igual a 2.

from funcoes_uteis import ler_num_int


def main():
    print('\n \t>>> Sequência de Fibonacci <<<')
    num = validar_num()
    print('')
    sequencia_fibonacci(num)


def validar_num():
    num = ler_num_int('->Digite o número limite da sequência: ')
    while True:
        if num >= 2:
            return num
        else:
            num = ler_num_int('''\nO número digitado é menor que 2. Tente novamente!! 
Digite um número (a partir de 2): ''')


def sequencia_fibonacci(num):
    quantidade_termos = 2
    ultimo = 1
    penultimo = 0

    print(f'{penultimo}, {ultimo}', end = '')
    while quantidade_termos < num:
        resultado = ultimo + penultimo
        penultimo = ultimo
        ultimo = resultado
        quantidade_termos += 1
        print(f', {resultado}', end = '')
    print(f'\n{'-'*40}')
        

main()