from funcoes_uteis import ler_num_int

def main():
    pessoa_maior_consumo = 0
    pessoa_menor_consumo = 0
    maior_consumo = 0
    menor_consumo = float('inf')

    alimentos = {
    'arroz': {'calorias': 130, 'proteinas': 2.7},
    'frango': {'calorias': 164, 'proteinas': 31},
    'carne bovina': {'calorias': 200, 'proteinas': 35},
    'peixe': {'calorias': 84, 'proteinas': 25}
    }
    qtd_pessoas = ler_num_int('Quantidade de pessoas para análise: ')

    for pessoa in range (1, qtd_pessoas + 1):
        total_calorias = 0
        total_proteinas = 0
        print(f'\n>>> CADASTRO {pessoa} <<<')
        qtd_alimentos = ler_num_int('Quantidade de alimentos a ser adicionada: ')
        
        for alimento in range (1, qtd_alimentos + 1):
            nome_alimento = validar_alimento('Nome do alimento: ', alimentos)
            qtd_gramas_consumidas = ler_num_int('Quantidade de gramas consumidas: ')
            
            valor_calorico = (qtd_gramas_consumidas/100) * alimentos[nome_alimento]['calorias']
            valor_proteico = (qtd_gramas_consumidas/100) * alimentos[nome_alimento]['proteinas']
            total_calorias += valor_calorico
            total_proteinas += valor_proteico

        print(f'\n--- {pessoa}ª PESSOA CADASTRADA ---')
        print(f'Total de calorias consumidas: {total_calorias}')
        print(f'Total de proteínas consumidas: {total_proteinas}')
        print(f'{35*'~'}')

        if total_calorias > maior_consumo:
            maior_consumo = total_calorias
            pessoa_maior_consumo = pessoa
        
        if total_calorias < menor_consumo:
            menor_consumo = total_calorias
            pessoa_menor_consumo = pessoa


    print(f'\n{5*' '}Pessoa com maior consumo: {pessoa_maior_consumo}')
    print(f'{5*' '}Pessoa com menor consumo: {pessoa_menor_consumo}')


def validar_alimento(label, lista_alimentos):
    nome_alimento = input(label)

    if nome_alimento.lower() in lista_alimentos:
        return nome_alimento
    else:
        print('Nome inválido, não encontrado na lista pré cadastrada. Tente novamente!')
        return validar_alimento(label, lista_alimentos)


main()