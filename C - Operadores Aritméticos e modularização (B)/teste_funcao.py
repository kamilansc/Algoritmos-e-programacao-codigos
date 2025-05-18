def principal():
    base = float(input("Digite a base em metros: "))
    altura = (float(input("Digite a altura em metros:")))
    resultado = area_triangulo(base, altura)
    print(resultado)


def area_triangulo(base, altura):
    # Processamento
    area = (base * altura) / 2

    # Saída
    return area

principal()

