from funcoes_uteis import ler_num_float, ler_num_int

def main():
    valor_inicial_divida = ler_num_float('Valor inicial da dívida: ')
    taxa_juros_mensal = ler_num_int('Taxa de juros mensal: ')
    qtd_meses_proj = ler_num_int('Quantidade de meses para projeção: ')
    saldo_divida = calc_juros_compt(valor_inicial_divida, taxa_juros_mensal)
    print(f'Dívida inicial com juros incidido do 1º mês: {saldo_divida}')

    for mes in range(1, qtd_meses_proj+1):
        pagamento = ler_num_float(f'\nPagamento do {mes}° mês: ')
        saldo_divida -= pagamento
        saldo_divida = calc_juros_compt(saldo_divida, taxa_juros_mensal)

        if saldo_divida <= 0.01:
            print(f'Dívida quitada no {mes}º mês de pagamento!')
            return
        
        print(f'''
    Dívida não quitada totalmente!
    SALDO REMANESCENTE: {saldo_divida:.2f}''')
    print(f'O pagamento não foi completado durante o período de {qtd_meses_proj} meses.')
        


def calc_juros_compt(capital, taxa):
    montante = capital * (1+taxa/100)**1
    return montante
    # travei na parte de calcular os juros compostos, não sei se devo calcular nessa parte ou calcular
    # toda vez que o usuário digitar um novo valor.



main()