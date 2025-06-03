from funcoes_uteis_copy3 import ler_num_racional_positivo

def main():
    n = ler_num_racional_positivo('Número: ')
    raiz = int(n**0.5)
    quadrado = raiz**2
    
    if quadrado == n:
        print(f'\n    A raiz quadrada de {n} é exata: {raiz} x {raiz} = {quadrado}')
    else:
        print(f'''
    A raiz quadrada de {n} é inexata.
    Maior quadrado possível: {quadrado} = {raiz} x {raiz}''')


main()