from funcoes_uteis import obter_numero_inteiro
import math

def main():
    num = validar_qtd_digitos()
    if eh_quadrado_perfeito(num):
        print(f'  >> {num} É um quadrado perfeito!')
    else:
        print(f'  >> {num} NÃO é um quadrado perfeito')


def validar_qtd_digitos():
    num = obter_numero_inteiro('Número: ')
    if len(str(num)) == 4:
        return num
    else:
        print('Número inválido, tente outra vez.\n')
        return validar_qtd_digitos()


def eh_quadrado_perfeito(num):
    return math.sqrt(num) == (int(num/100) + int(num%100))


if __name__ == '__main__':
    main()