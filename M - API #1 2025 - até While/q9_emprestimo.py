from q3_float_utils import obter_num_float_positivo, obter_num_float_minimo
from q2_int_utils import obter_num_int_in_faixa

def main():
    # montante = juros + capital
    #juros = capital * taxa * tempo
    renda_mensal = obter_num_float_positivo('Renda mensal do cliente: ')
    valor_emprestimo = obter_num_float_minimo('Valor do empréstimo: ', 1518)
    prazo = obter_num_int_in_faixa('Prazo de pagamento desejado: ', 2, 24)

    IOF = calcular_IOF(valor_emprestimo, prazo)

    capital = valor_emprestimo + IOF

    juros = calcular_juros(capital, prazo)

    total_pagar = juros + capital
    valor_parcela = total_pagar/prazo
    parcela_maxima = (30/100)*renda_mensal 

    if valor_parcela <= 0.3*renda_mensal:
        situacao_emprestimo = 'APROVADO'
    elif valor_parcela > 0.3*renda_mensal:
        situacao_emprestimo = 'REPROVADO'

# saída
    print(f'''
    a. IOF: R$ {IOF:.2f}
    b. Juros a pagar: R$ {juros:.2f}
    c. Total a pagar: R$ {total_pagar:.2f}
    d. Parcela: {prazo}x de R$ {valor_parcela:.2f}
    e. Parcela máxima: R$ {parcela_maxima:.2f};
       Situação do empréstimo: {situacao_emprestimo}''')


def calcular_IOF(valor_emprestimo, prazo):
    qtd_dias_prazo = 30*prazo
    IOF = ((0.38/100)*valor_emprestimo) + (0.0082/100)*qtd_dias_prazo * valor_emprestimo
    return IOF


def calcular_juros(capital, prazo):
    taxa = analisar_situacao_selic(prazo)
    juros = capital * taxa * prazo
    return juros


def analisar_situacao_selic(prazo):
    SELIC = 14.75/100

    if prazo <= 6:
        return 0.5*SELIC
    elif prazo < 12:
        return 0.75*SELIC
    elif prazo <= 18:
        return SELIC
    elif prazo > 18:
        return 1.3*SELIC


main()