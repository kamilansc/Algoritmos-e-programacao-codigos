from funcoes_uteis_copy3 import ler_num_int_positivo

def main():
    print('>> CALCULADORA DE FATORIAL <<')
    num = ler_num_int_positivo('Número: ')
    saida = f'{num}! = '

    fatorial = 1
    for i in range(num, 0, -1):
        fatorial *= i
        if i > 1:
            saida += f'{i} x '
        else:
            saida += f'{i}'

    
    print(f'{saida} = {fatorial}')


main()