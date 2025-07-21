def main():
    x, y = map(int, input().split())

    contador = 0
    linha = []
    for num in range(1, y+1):
        if contador > x:
            contador = 1
            print(f'{' '.join(linha)}\n')
            linha.clear()
        
        while contador <= x:
            linha.append(str(num))
            contador += 1

            break


main()