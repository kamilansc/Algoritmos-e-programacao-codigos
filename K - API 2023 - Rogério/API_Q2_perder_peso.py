from funcoes_uteis_copy1 import ler_num_racional_min, ler_num_int_min, ler_num_int, ler_num_racional

def main():
    peso_atual = ler_num_racional_min('Digite o seu peso atual: ', 1)

    sexo = ler_num_int('Digite o seu sexo (1 - feminino / 2 - masculino): ')
    sexo = validar_sexo(sexo)

    kg_perder = ler_num_racional_min('Digite quantos quilos quer perder: ', 0.1) * 7000
    qtd_dias_treino = ler_num_int_min('Digite quantos dias por semana irá treinar: ', 1)
    qtd_tempo_dia = ler_num_racional('Digite quantas horas irá treinar por dia: ')*60

    proporcao_transport = ler_num_racional('Digite qual a proporção de tempo (em %) alocada para o exercício "transport": ')/100
    proporcao_escada = 1 - proporcao_transport

    tmp_dia_transport = proporcao_transport * qtd_tempo_dia
    tmp_dia_escada = proporcao_escada * qtd_tempo_dia

    calcular_perda_peso(sexo, kg_perder, qtd_dias_treino, tmp_dia_transport, tmp_dia_escada)


def calcular_perda_peso(sexo, kg_perder, qtd_dias_treino, tmp_dia_transport, tmp_dia_escada):
    if sexo == 1:
        calorias_gasta_transport = (tmp_dia_transport/6)*100
        calorias_gasta_escada = (tmp_dia_escada/8)*100
        qtd_total_calorias_dia = calorias_gasta_escada + calorias_gasta_transport
        qtd_semanas_resultado = (kg_perder/qtd_total_calorias_dia)/qtd_dias_treino
    elif sexo == 2:
        calorias_gasta_transport = (tmp_dia_transport/5)*100
        calorias_gasta_escada = (tmp_dia_escada/7)*100
        qtd_total_calorias_dia = calorias_gasta_escada + calorias_gasta_transport
        qtd_semanas_resultado = (kg_perder/qtd_total_calorias_dia)/qtd_dias_treino
#    else:
#        print(f'A opção digitada "{sexo} não está cadastrada. Tente novamente!')
#        return calcular_perda_peso(sexo, kg_perder, qtd_dias_treino, tmp_dia_transport, tmp_dia_escada)

    print(f'''
Você conseguirá perder os {(kg_perder/7000):.1f}kg desejados em um tempo de {qtd_semanas_resultado:.0f} semanas aproximadamente;
para isso, você deverá cumprir diariamente {tmp_dia_transport:.0f} minutos de "transport" e {tmp_dia_escada:.0f} minutos de "simulador de escada".
To torcendo por você!! Fighting S2''')


def validar_sexo(sexo):
    if sexo not in [1, 2]:
        print(f'A opção digitada "{sexo}" não está cadastrada. Tente novamente!')
        sexo = ler_num_int('Digite o seu sexo (1 - feminino / 2 - masculino): ') 
        return validar_sexo(sexo)
    return sexo


main()