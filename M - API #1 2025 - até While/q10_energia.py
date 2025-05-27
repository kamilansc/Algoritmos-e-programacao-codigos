from q02_int_utils import obter_num_int_positivo
from q04_text_utils import obter_texto
from q03_float_utils import obter_num_float_positivo

def main():
    qtd_familias = obter_num_int_positivo('Quantidade de famílias: ')

    while qtd_familias > 0:
        consumidor = obter_texto('Consumidor: ')
        consumo_familia = obter_num_float_positivo('Consumo: ')

        if consumo_familia <= 30:
            valor_KWh = 0
        elif consumo_familia > 200:
            valor_KWh = 0.89 + 0.3*0.89
        else:
            valor_KWh = 0.89
        
        valor_total_kwh = situacao_consumo(consumo_familia)
        
        tarifa_iluminacao = calcular_tarifa_ilum(valor_total_kwh)

        valor_ICMS = 0.25*valor_total_kwh
        valor_PIS_COFINS = (3.75/100)*valor_total_kwh

        total_pagar = valor_total_kwh + tarifa_iluminacao + valor_ICMS + valor_PIS_COFINS

        print(f'''
        {6*'*'} TALÃO MENSAL XPTO {6*'*'}
        Consumidor: {consumidor}
        Consumo(KWh): {consumo_familia}
        Consumo(R$): R$ {valor_total_kwh:.2f} (valor por KWh: R$ {valor_KWh:.2f})
        Bandeira Tarifária: R$ 0.00 (valor por 100KWh: R$ 0.00)
        Total sem impostos: R$ {valor_total_kwh:.2f}
        ICMS: R$ {valor_ICMS:.2f}
        PIS/COFINS: R$ {valor_PIS_COFINS:.2f}
        Iluminação Pública: R$ {tarifa_iluminacao:.2f}
        {30*'-'}
        Total a pagar: R$ {total_pagar:.2f}
''')

        qtd_familias -= 1


def situacao_consumo(consumo):
    valor_total_kwh = consumo * 0.89

    if consumo <= 30:
        valor_total_kwh = 0

    elif consumo > 200:
        valor_kwh = 0.89 + 0.3*0.89
        valor_total_kwh = consumo*valor_kwh

    return valor_total_kwh


def calcular_tarifa_ilum(valor_total):
    if valor_total > 0:
        tarifa_iluminacao = 0.03*valor_total
    else:
        tarifa_iluminacao = 0
    
    return tarifa_iluminacao


main()