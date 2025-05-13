from funcoes_uteis import ler_num_int

def main():
    num = ler_num_int('Digite um número (denominador): ')

    i = 1
    soma = 0
    
    print('--> Frações:')
    while i <= num:
        numerador = (-1)**(i+1)
        soma += numerador/i
        print(f'{numerador}/{i} = \t {(numerador/i):.2f} \t soma atual: {soma:.2f}')
        i += 1
    print(f'soma final: {soma:.2f}')


main()