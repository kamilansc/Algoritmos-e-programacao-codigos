#Copie o loop de “Raízes quadradas”, na página 111, e encapsule-o em uma função chamada mysqrt que receba a como parâmetro, 
# escolha um valor razoável de x e devolva uma estimativa da raiz quadrada de a.
# Para testar, escreva uma função denominada test_square_root, que exibe uma tabela como esta:


def main():
    a = int(input('Digite um número para descobrir a raiz dele: '))
    print(mysqrt(a))
    test_square_root()


def mysqrt(a):
#    x = int(input('Digite um valor que voçê estima ser a raiz quadrada: '))
    if a > 1:
        x = a / 2
    else:
        a = 1
    
    epsilon = 1e-15

    while True:
        y = (x + a/x) / 2
        print('x:', x, '\t', 'y:', y)
        if abs(y - x) < epsilon:
            return 'y:', y
        x = y


def test_square_root():
    print(f'{'a': <5}  {'mysqrt(a)': <14} {'math.mysqrt(a)': <19} {'diff': <9}')
    print(f"{'-'*5} {'-'*11}   {'-'*17}  {'-'*8}")


main()