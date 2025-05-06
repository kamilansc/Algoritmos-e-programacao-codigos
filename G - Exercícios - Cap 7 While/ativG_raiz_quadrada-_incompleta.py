def main():
    a = int(input('Digite um número para descobrir a raiz dele: '))
    x = int(input('Digite um valor que voçê estima ser a raiz quadrada: '))

    while True:
        y = (x + a/x) / 2
        print('x:', x, '\t', 'y:', y)
        if x == y:
            break
        x = y


main()