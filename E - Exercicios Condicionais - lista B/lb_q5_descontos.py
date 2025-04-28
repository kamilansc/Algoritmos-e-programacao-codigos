'''Exercício 5: Calculadora de Descontos
Crie um programa para uma loja que calcule o preço final de um produto com base
em regras de desconto:

● Compras acima de R$ 500,00: 15% de desconto ✔
● Compras entre R$ 200,00 e R$ 500,00: 10% de desconto ✔
● Compras entre R$ 100,00 e R$ 199,99: 5% de desconto ✔
● Cliente VIP: desconto adicional de 5% (acumulativo) ✔
● Cliente Aniversariante: desconto adicional de 3% (acumulativo) ✔

Conhecimentos Necessários:
● Combinação de expressões booleanas
● Cálculos percentuais
● Estruturas condicionais aninhadas

Estrutura Sugerida:
1. Função para calcular desconto base (pelo valor) ✔
2. Função para calcular desconto adicional (VIP e aniversariante) ✔
3. Função para calcular preço final
4. Função principal para interação com usuário ✔'''

from funcoes_uteis import obter_numero_racional

def main():
    preco = obter_numero_racional('Digite o preço do produto: ')
    desconto_base = calcular_desconto_base(preco)
    desconto_adicional = calcular_desconto_adicional(preco)
    preco_liquido = calcular_preco_final(preco, desconto_base, desconto_adicional)
    print(f'Preço líquido com os descontos: R${preco_liquido}')


def calcular_desconto_base(preco):
    if preco >= 100 and preco <= 199.99:
        return 5/100 * preco
    elif preco <= 500:
        return 10/100 * preco
    elif preco > 500:
        return 15/100 * preco


def calcular_desconto_adicional(preco):
    entrada = input('Você é cliente Vip (Responda Sim ou Não): ')
    entrada2 = input('Você é aniversariante hoje (Responda Sim ou Não): ')
    if (entrada == 'Sim' or entrada == 'sim') and (entrada2 == 'Sim' or entrada2 == 'sim'):
        return (5/100 * preco) + (3/100 * preco)
    elif (entrada == 'Não' or entrada == 'não') and (entrada2 == 'Não' or entrada2 == 'não'):
        return 0
        
    elif (entrada == 'Sim' or entrada == 'sim') and (entrada2 == 'Não' or entrada2 == 'não'): 
        return 5/100 * preco
    elif (entrada == 'Não' or entrada == 'não') and (entrada2 == 'Sim' or entrada2 == 'sim'): 
        return 3/100 * preco
    else:
        print('O valor digitado não está cadastrado. Tente novamente')
        return calcular_desconto_adicional(preco)

    

def calcular_preco_final(preco, desconto_base, desconto_adicional):
    return preco - desconto_base - desconto_adicional


main()

    