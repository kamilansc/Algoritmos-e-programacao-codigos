# 6. Leia 3 (três) números (cada número corresponde a um ângulo interno do triângulo), verifique e escreva se os 3 (três) números formam um triângulo (a soma dos 
# ângulos internos é igual a 180o). Se formam, verifique se formam um triângulo acutângulo (3 ângulos < 90o), retângulo (1 ângulo = 90o) ou obtusângulo (1 ângulo > 
# 90o). Não existe ângulo com tamanho 0o (zero grau).

from funcoes_uteis import obter_numero_exceto_zero

def main():
    label = 'Digite um número (correspondendo ao ângulo interno do triângulo): '
    numero1 = (obter_numero_exceto_zero(label))
    numero2 = (obter_numero_exceto_zero(label))
    numero3 = (obter_numero_exceto_zero(label))
    print(f'Ângulos digitados: {numero1}, {numero2}, {numero3} \n')

    if eh_triangulo(numero1, numero2, numero3):
        if classifica_triangulo(numero1, numero2, numero3) == 1:
            print('É um triângulo acutângulo')
        elif classifica_triangulo(numero1, numero2, numero3) == 2:
            print('É um triângulo retângulo')
        elif classifica_triangulo(numero1, numero2, numero3) == 3:
            print('É um triângulo obtusângulo')
    else:
        print('Opss. Isso definitivamente não é um triângulo retângulo!! Tente novamente')
        return main()
    

def eh_triangulo(lado_a, lado_b, lado_c):
    return lado_a + lado_b + lado_c == 180

def classifica_triangulo(lado_a, lado_b, lado_c):
    if lado_a < 90 and lado_b < 90 and lado_c < 90:
        return 1
    elif lado_a == 90 or lado_b == 90 or lado_c == 90:
        return 2
    elif lado_a > 90 or lado_b > 90 or lado_c > 90:
        return 3

main()