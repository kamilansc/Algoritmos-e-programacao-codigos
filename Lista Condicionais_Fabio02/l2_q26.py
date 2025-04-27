# 26. Leia os 3 (três) lados de um triângulo e identifique sua hipotenusa e seus catetos.

from l2_q15_horas_aulas import obter_numero_racional

def main():
    lado1 = obter_numero_racional('Digite o primeiro lado: ')
    lado2 = obter_numero_racional('Digite o segundo lado: ')
    lado3 = obter_numero_racional('Digite terceiro lado: ')

    print(analisar_lados(lado1, lado2, lado3))


def analisar_lados(l1, l2, l3):
    if l1 > l2 and l1 > l3:
        return f'O lado "{l1}" é a hipotenusa e os lados {l2} e {l3} são os catetos'
    elif l2 > l1 and l2 > l3:
        return f'O lado "{l2}" é a hipotenusa e os lados {l1} e {l3} são os catetos'
    elif l3 > l1 and l3 > l2:
        return f'O lado "{l3}" é a hipotenusa e os lados {l1} e {l2} são os catetos'


main()