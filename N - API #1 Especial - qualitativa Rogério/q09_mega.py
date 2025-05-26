# Início: 25/05 - 21h24
# Fim:    25/05 - 22h

from q01_number_utils import obter_num_int, obter_num_int_positivo

def main():
    premio = obter_num_int('Valor do prêmio: ')

    valor_individual_anterior = 0
    valor_total = 0
    while True:
        valor_individual_atual = obter_num_int_positivo('Valor individual do amigo: ')
        if valor_individual_atual == 0:
            break
        valor_total += valor_individual_atual

        if valor_individual_atual > valor_individual_anterior:
            maior_valor_individual = valor_individual_atual
        
        if valor_individual_atual < valor_individual_anterior:
            menor_valor_individual = valor_individual_atual

        valor_individual_anterior = valor_individual_atual

    print(valor_total)
    imposto = (20/100)*premio
    premio_descontado = premio - imposto

    maior_premio_individual = (maior_valor_individual/valor_total)*premio_descontado
    menor_premio_individual = (menor_valor_individual/valor_total)*premio_descontado


    print(f'''
        Maior prêmio individual: {maior_premio_individual:.1f}
        Menor prêmio individual: {menor_premio_individual:.1f}''')


main()