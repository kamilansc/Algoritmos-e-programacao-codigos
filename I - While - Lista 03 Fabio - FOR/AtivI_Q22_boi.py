from funcoes_uteis import ler_num_int, ler_num_racional

def main():
    num_fichas = ler_num_int('Digite o número de fichas: ')
    identificar_bois(num_fichas)


def identificar_bois(num_fichas: int):
    contador = 0
    peso_boi = 0
    boi_mais_gordo = 0
    num_boi_mais_gordo = 0
    boi_mais_magro = 99999
    numero_boi_magro = 0
    nome_boi = None

    while contador < num_fichas:
        num_boi = ler_num_int('Digite o número do boi: ')
        peso_boi = ler_num_racional('Digite o peso do boi: ')
        nome_boi = input('Digite o nome do boi:')
        print('')
        contador += 1

        if peso_boi > boi_mais_gordo:
            boi_mais_gordo = peso_boi
            num_boi_mais_gordo = num_boi
            nome_boi_mais_gordo = nome_boi
        
        

        if peso_boi < boi_mais_magro:
            boi_mais_magro = peso_boi
            numero_boi_magro = num_boi
            nome_boi_mais_magro = nome_boi

        

    print(f'''
    Número do boi mais gordo: {num_boi_mais_gordo}
    Peso do boi mais gordo: {boi_mais_gordo}
    Nome do boi mais gordo: {nome_boi_mais_gordo}

    Número do boi mais magro: {numero_boi_magro}
    Peso do boi mais magro: {boi_mais_magro}
    Nome do boi mais magro: {nome_boi_mais_magro}
    ''')


main()