# 20. Leia a medida de um ângulo (entre 0 e 360°) e escreva o quadrante (primeiro, segundo, terceiro ou
# quarto) em que o ângulo se localiza.

'''O primeiro quadrante vai de 0° a 90° (ou 0 a π/2 radianos), o segundo de 90° a 180° (π/2 a π), o terceiro de 180° a 270° (π a 3π/2)
e o quarto de 270° a 360° (3π/2 a 2π). Se o ângulo for maior que 360°, basta subtrair 360° até obter um valor entre 0° e 360'''

from l2_q15_horas_aulas import obter_numero_racional

def main():
    angulo = obter_numero_racional('Digite a medida do ângulo (entre 0 e 360°): ')
    quadrante = identificar_quadrante(angulo)
    print(f'O ângulo {angulo}° está no {quadrante}')


def identificar_quadrante(angulo):
    if angulo < 0 and angulo <= 90:
        return '1º quadrante'
    elif angulo <= 180:
        return '2º quadrante'
    elif angulo <= 270:
        return '3º quadrante'
    elif angulo <= 360:
        return '4º quadrante'


main()
