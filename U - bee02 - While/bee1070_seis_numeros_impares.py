def main():
    x = int(input())
    contador = 1

    while contador <= 6:
        if eh_impar(x):
            print(x)
            contador += 1
        x += 1
    

def eh_impar(x):
    return x % 2 != 0


main()