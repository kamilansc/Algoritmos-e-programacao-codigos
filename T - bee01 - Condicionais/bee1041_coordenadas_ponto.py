def main():
    coordenadas_ponto = input().split()
    coord_x = float(coordenadas_ponto[0])
    coord_y = float(coordenadas_ponto[1])

    if coord_x == 0 and (coord_y > 0 or coord_y < 0):
        print('Eixo Y')
        return
    elif coord_y == 0 and (coord_x > 0 or coord_x < 0):
        print('Eixo X')
        return
    
    elif coord_x == 0 and coord_y == 0:
        print('Origem')
        return
    
    elif coord_x > 0 and coord_y > 0:
        quadrante = 'Q1'
    elif coord_x < 0 and coord_y > 0:
        quadrante = 'Q2'
    elif coord_x < 0 and coord_y < 0:
        quadrante = 'Q3'
    elif coord_x > 0 and coord_y < 0:
        quadrante = 'Q4'

    print(quadrante)


main()