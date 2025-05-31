from funcoes_uteis_copy2 import ler_num_racional_positivo

def main():
    prod1 = ler_num_racional_positivo('Valor do 1º produto: ')
    prod2 = ler_num_racional_positivo('Valor do 2º produto: ')
    prod3 = ler_num_racional_positivo('Valor do 3º produto: ')

    print(f'''
    -- Valores informados --
    Produto 1: R$ {prod1}
    Produto 2: R$ {prod2}
    Produto 3: R$ {prod3}''')

    if prod1 <= prod2 and prod1 <= prod3:
        print(f'Compensa mais comprar o produto 1 de R$ {prod1:.2f}'.rjust(48))
    elif prod2 <= prod1 and prod2 <= prod3:
        print(f'Compensa mais comprar o produto 2 de R$ {prod2:.2f}'.rjust(48))
    else:
        print(f'Compensa mais comprar o produto 3 de R$ {prod3:.2f}'.rjust(48))


main()