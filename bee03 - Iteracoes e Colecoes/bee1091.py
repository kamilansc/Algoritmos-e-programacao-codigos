def main():
    qtd_casos_teste = int(input())

    saida = []
    while qtd_casos_teste != 0:
        coordenadas_ponto_divisor = input().split()
        ponto_horizontal = int(coordenadas_ponto_divisor[0])
        ponto_vertical = int(coordenadas_ponto_divisor[1])

        for teste in range(qtd_casos_teste):
            coordenadas_casa = input().split()
            ponto_x = int(coordenadas_casa[0])
            ponto_y = int(coordenadas_casa[1])

            if ponto_x == ponto_horizontal or ponto_y == ponto_vertical:
                saida .append('divisa')
            elif ponto_x < ponto_horizontal and ponto_y > ponto_vertical:
                saida.append('NO')
            elif ponto_x > ponto_horizontal and ponto_y > ponto_vertical:
                saida.append('NE')
            elif ponto_x > ponto_horizontal and ponto_y < ponto_vertical:
                saida.append('SE')
            elif ponto_x < ponto_horizontal and ponto_y < ponto_vertical:
                saida.append('SO')
        
        qtd_casos_teste = int(input())
    
    print('\n'.join(saida))


main()