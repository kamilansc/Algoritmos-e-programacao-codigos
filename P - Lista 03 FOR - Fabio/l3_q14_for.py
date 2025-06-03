from funcoes_uteis_copy3 import ler_num_racional_positivo

def main():
    n = ler_num_racional_positivo('Número: ')
    print(calcular_quadrado(n))
    

def calcular_quadrado(n):
    maior_quadrado = 0
    for num in range(1, int((n**0.5))+1):
        if num**2 == n:
            return f'Quadrado igual {n} = {num} x {num} = {num**2}'
        elif num**2 < n:
            maior_quadrado = num**2

    return f'Menor quadrado possível: {maior_quadrado**0.5} x {maior_quadrado**0.5} = {maior_quadrado}'


main()