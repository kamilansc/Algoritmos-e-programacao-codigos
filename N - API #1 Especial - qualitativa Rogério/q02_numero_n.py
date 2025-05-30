from q01_number_utils import obter_num_int_positivo, obter_num_int

def main():
    n = obter_num_int_positivo('Quantidade de sequências: ')

    processar_sequencias(n)
    

def processar_sequencias(qtd_sequencia):
    soma_numeros = 0
    qtd_numeros_digitados = 0
    maior_numero = float('-inf')
    menor_numero = float('inf')

    while qtd_sequencia > 0:

        soma_sequencia_pares = 0
        while True:
            num = obter_num_int('Número: ')
            if num == 0:
                print(f'Soma dos pares da sequência: {soma_sequencia_pares}')
                break

            elif num % 2 == 0:
                soma_sequencia_pares += num
            
            qtd_numeros_digitados += 1
            soma_numeros += num

            if num > maior_numero:
                maior_numero = num
            if num < menor_numero:
                menor_numero = num

        qtd_sequencia -= 1

        if qtd_sequencia > 0:
            print('\n>>> Próxima sequência')

    if qtd_numeros_digitados > 0:
        media_numeros = soma_numeros/qtd_numeros_digitados
    else:
        maior_numero = 0
        media_numeros = 0
        menor_numero = 0

    print(f'''
        Média: {media_numeros:.1f}
        Maior número: {maior_numero}
        Menor número: {menor_numero}''')

main()