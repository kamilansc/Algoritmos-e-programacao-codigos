def principal():
    valor_mercadoria = float(input("Digite o valor da mercadoria: "))
    parcela = calcular_parcelas(valor_mercadoria)
    entrada = valor_mercadoria - (2*parcela)
    print(f"""  
    Valor da mercadoria: R$ {valor_mercadoria:.2f};
    Parcelas: R$ {parcela:.2f}
    Valor da entrada: R${entrada:.2f}""")

def calcular_parcelas(valor_mercadoria):
    parcela = valor_mercadoria // 3
    return parcela

principal()