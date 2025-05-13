'''
A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e
número de filhos. Escreva um algoritmo que leia o salário e o número de filhos de N habitantes e
escreva:
a) média de salário da população;
b) média de número de filhos;
c) percentual de pessoas com salário de até R$ 1.000,00.'''

from funcoes_uteis import ler_num_int, ler_num_racional


def main():
    qtd_entrevistados = ler_num_int('Digite a quantidade de habitantes: ')
    armazenar_dados(qtd_entrevistados)


def armazenar_dados(qtd_entrevistados):
    contador = 0
    baixa_renda = 0
    soma_salario = 0
    soma_qtd_filhos = 0

    while contador < qtd_entrevistados:
        salario = ler_num_racional('Digite o salário: ')
        qtd_filhos = ler_num_int('Digite a quantidade de filhos: ')
        print('')
        soma_qtd_filhos += qtd_filhos
        soma_salario += salario
        contador += 1

        if salario <= 1000:
            baixa_renda += 1
        
    media_salario = soma_salario/qtd_entrevistados
    media_qtd_filhos = soma_qtd_filhos/qtd_entrevistados
    percentual_baixa_renda = (baixa_renda/qtd_entrevistados)*100

    print(f'''
- Quantidade de entrevistados: {qtd_entrevistados}
- Media do salario: {media_salario:.2f}
- Media da quantidade de filhos: {media_qtd_filhos}
- Percentual de pessoas quantidades: {percentual_baixa_renda:.1f}''')


main()

