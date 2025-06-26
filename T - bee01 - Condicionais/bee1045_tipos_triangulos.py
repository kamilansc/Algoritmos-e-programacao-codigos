def main():
    entrada = list(map(float, input().split()))
    entrada.sort(reverse=True)
    A, B, C = entrada

    if A >= B+C:
        print('NAO FORMA TRIANGULO')
        return
    if abs(A**2 - (B**2 + C**2)) < 1e-9:
        print('TRIANGULO RETANGULO')
    elif A**2 > B**2 + C**2:
        print('TRIANGULO OBTUSANGULO')
    elif A**2 < B**2 + C**2:
        print('TRIANGULO ACUTANGULO')

    if A == B and A == C:
        print('TRIANGULO EQUILATERO')
    elif A == B or A == C or B == C:
        print('TRIANGULO ISOSCELES')


main()