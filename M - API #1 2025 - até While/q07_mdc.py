from q02_int_utils import obter_num_int_positivo

def main():
    print(f'''
{6*'*'} ALGORITMO DE EUCLIDES {6*'*'}
     MÁXIMO DIVISOR COMUM (MDC)
''')

    num1 = obter_num_int_positivo('1º número: ')
    num2 = obter_num_int_positivo('2º número: ')

    print(f'MDC de {num1} e {num2}: {descobrir_mdc(num1, num2)}')


def descobrir_mdc(num1, num2):
    while True:
        resto = num1 % num2
        if resto == 0:
            resto = num2
            return resto
        
        num1 = num2
        num2 = resto
    

main()