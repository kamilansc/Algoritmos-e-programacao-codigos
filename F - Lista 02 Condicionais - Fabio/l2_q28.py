# Leia as coordenadas cartesianas (x e y) de 2 (dois) pontos no plano, que corresponderão a dois cantos de
# um retângulo. Baseado nisto, calcule e escreva a área deste retângulo. Lembre-se de que o valor da área
# não pode ser negativo.

def main():
    x1 = float(input("Digite a coordenada x do primeiro ponto: "))
    y1 = float(input("Digite a coordenada y do primeiro ponto: "))
    x2 = float(input("Digite a coordenada x do segundo ponto: "))
    y2 = float(input("Digite a coordenada y do segundo ponto: "))

    base = calc_area_retangulo(x1, y1, x2, y2)
    print(f'\n >> A área do triângulo é {base}')


def calc_area_retangulo(x1, y1, x2, y2):
    base = abs(x2 - x1)
    altura = abs(y2 - y1)
    return base*altura


main()