def main():
    menu = f'''
    CÓDIGO   {'ESPECIFICAÇÃO'.ljust(20)}PREÇO
    1        {'Cachorro Quente'.ljust(20)}R$ 4.00
    2        {'X-Salada'.ljust(20)}R$ 4.50
    3        {'X-Bacon'.ljust(20)}R$ 5.00
    4        {'Torrada Simples'.ljust(20)}R$ 2.00
    5        {'Refrigerante'.ljust(20)}R$ 1.50'''
    print(menu)
    entrada = input()
    cod_produto = int(entrada.split()[0])
    qtd_produto = int(entrada.split()[1])

    if cod_produto == 1:
        total = 4*qtd_produto
    elif cod_produto == 2:
        total = 4.5*qtd_produto
    elif cod_produto == 3:
        total = 5*qtd_produto
    elif cod_produto == 4:
        total = 2*qtd_produto
    elif cod_produto == 5:
        total = 1.5*qtd_produto

    print(f'Total: R$ {total:.2f}')


main()