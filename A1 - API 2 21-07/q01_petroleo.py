from utils import obter_num_inteiro, obter_num_float

def main():
    qtd_bombas = obter_num_inteiro('Quantidade de bombas: ')
    valor_inicial_barris = obter_num_inteiro('Quantidade inicial de barris: ')
    percent_reducao = obter_num_float('Valor de redução na quantidade por ciclo (em %): ')
    percent_reducao /= 100
    limite_min_bomba = obter_num_inteiro('Limite mínimo de barris permitido por bomba: ')

    qtd_barris_total, qtd_ciclos = calcular_extração_petroleo(qtd_bombas, valor_inicial_barris,\
                                    percent_reducao, limite_min_bomba)
    
    print(f'Qtd total de barris: {qtd_barris_total:.1f}')
    print(f'Qtd ciclos: {qtd_ciclos}')


def calcular_extração_petroleo(qtd_bombas, valor_inicial_barris, percent_reducao, limite_min):
    qtd_extraida = valor_inicial_barris
    qtd_barris_ciclo = 0
    qtd_ciclos = 0

    while qtd_extraida >= limite_min:
        print(qtd_extraida)
        print(qtd_ciclos)
        qtd_ciclos += 1
        qtd_barris_ciclo += qtd_extraida
        qtd_extraida -= qtd_extraida*percent_reducao
    
    qtd_barris_total = qtd_barris_ciclo * qtd_bombas

    return qtd_barris_total, qtd_ciclos


main()