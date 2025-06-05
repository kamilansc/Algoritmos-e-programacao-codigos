from funcoes_uteis import ler_num_float, ler_num_int

def main():
    valor_inicial_divida = ler_num_float('Valor inicial da dívida: ')
    taxa_juros_mensal = ler_num_int('Taxa de juros mensal: ')/100
    qtd_meses_proj = ler_num_int('Quantidade de meses para projeção: ')

    # travei na parte de calcular os juros compostos, não sei se devo calcular nessa parte ou calcular
    # toda vez que o usuário digitar um novo valor.



main()