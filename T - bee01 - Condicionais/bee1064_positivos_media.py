def main():
    qtd_positivos = 0
    somatorio_positivos = 0
    for i in range (1, 6+1):
        valor = float(input())

        if valor > 0:
            qtd_positivos += 1
            somatorio_positivos += valor
    
    media_positivos = somatorio_positivos/qtd_positivos
    
    print(f'''{qtd_positivos} valores positivos
{media_positivos:.1f}''')


main()