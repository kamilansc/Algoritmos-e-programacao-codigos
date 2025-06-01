from funcoes_uteis_copy3 import ler_num_int_positivo

def main():
    num = ler_num_int_positivo('Número: ')
    print(f'*** SOMATÓRIO DE 1 A {num} ***')
    saida = ''

    somatorio = 0  
    for i in range (1, num+1):
        somatorio += i
        
        if i == num:
            saida += f'{i}'
        else:
            saida += f'{i} + '
    
    print(f'{saida} = {somatorio}')


main()