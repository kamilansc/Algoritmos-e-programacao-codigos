# Contexto/Problema: Para um controle financeiro mais rigoroso, é necessário registrar todas as
# receitas e despesas de um mês. O programa deve permitir que o usuário insira múltiplas receitas e
# múltiplas despesas. Para cada transação (seja receita ou despesa), o usuário deve informar uma
# descrição e o valor. Ao final, o programa deve apresentar o total de receitas, o total de despesas, o
# saldo final do mês e categorizar a despesa de maior valor e a receita de maior valor.

# ● Entrada: O usuário deve informar a quantidade de receitas a serem cadastradas e, para cada uma, a
# descrição e o valor. Em seguida, o usuário deve informar a quantidade de despesas a serem
# cadastradas e, para cada uma, a descrição e o valor.

# ● Saída Esperada: O total de receitas, o total de despesas, o saldo final do mês. A descrição e o valor da
# maior receita e da maior despesa.

from funcoes_uteis import ler_num_int, ler_num_float, ler_texto

def main():
    qtd_receitas = ler_num_int('Quantidade de receitas a serem cadastradas: ')
    
    valor_total_receita = 0
    valor_maior_receita = 0
    for num in range(1, qtd_receitas+1):
        print(f'--- {num}ª RECEITA ---')
        valor_receita = ler_num_float(f'Valor da receita: ')
        descricao_receita = ler_texto(f'Descrição da receita: ')
        
        valor_total_receita += valor_receita

        if valor_maior_receita == 0 or valor_receita > valor_maior_receita:
            valor_maior_receita = valor_receita
            id_maior_receita = num
            desc_maior_receita = descricao_receita
    
    qtd_despesas = ler_num_int('Quantidade de despesas a serem cadastradas: ')

    valor_total_despesa = 0
    valor_maior_despesa = 0
    for indice in range(1, qtd_despesas+1):
        print(f'\n---{indice}ª DESPESA ---')
        valor_despesa = ler_num_float('Valor da despesa: ')
        descricao_despesa = ler_texto('Descrição da despesa: ')

        valor_total_despesa += valor_despesa

        if valor_maior_despesa == 0 or valor_despesa > valor_maior_despesa:
            valor_maior_despesa = valor_despesa
            id_maior_despesa = indice
            desc_maior_despesa = descricao_despesa

    saldo_final = valor_total_receita - valor_total_despesa

    info_receitas = f'''
    Total de receitas: {qtd_receitas}
    Total de despesas: {qtd_receitas}
    Saldo final: R$ {saldo_final}
    >>> Maior receita:
        Nº: {id_maior_receita}
        Valor: {valor_maior_receita}
        Descrição: {desc_maior_receita}

    >>> Maior despesa:
        Nº: {id_maior_despesa}
        Valor: {valor_maior_despesa}
        Descrição: {desc_maior_despesa}
    '''

    print(info_receitas)


main()

    