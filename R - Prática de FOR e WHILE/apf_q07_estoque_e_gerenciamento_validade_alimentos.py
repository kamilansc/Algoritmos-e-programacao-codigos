from funcoes_uteis import ler_num_int, ler_texto

def main():
    qtd_alimentos_cadastrar = ler_num_int('Quantidade de alimentos para cadastrar: ')

    lista_alimentos = []
    for alimento in range(1, qtd_alimentos_cadastrar+1):
        situacao_item = None
        nome = ler_texto('Nome do alimento: ')
        qtd_alimento = ler_num_int(f'Quantidade obtida do item "{nome}": ')
        data_compra = ler_texto('Data de compra (formato aceito: DD/MM/AAAA): ')
        data_validade = ler_texto('Data de validade do item (formato aceito: DD/MM/AAAA): ')

        valores_compra = data_compra.split('/')
        dia_compra = int(valores_compra[0])
        mes_compra = int(valores_compra[1])
        ano_compra = int(valores_compra[2])

        valores_validade = data_validade.split('/')
        dia_validade = int(valores_validade[0])
        mes_validade = int(valores_validade[1])
        ano_validade = int(valores_validade[2])

        if ano_compra > ano_validade:
            situacao_item = 'Vencido'

        elif ano_compra == ano_validade:
            if mes_compra > mes_validade:
                situacao_item = 'Vencido'
            elif mes_compra == mes_validade:
                if dia_compra > dia_validade:
                    situacao_item = 'Vencido'
                else:
                    situacao_item = 'Validade próxima'
                    
        if situacao_item != None:
            lista_alimentos.append(f'Item: {nome}\t| Validade: {data_validade}\t| Situação do item: {situacao_item}')

    print('\n'.join(lista_alimentos))            


main()