# Início 25/05 - 17h05
# Fim 25/05 - 19h25

from q1_number_utils import obter_num_int_in_faixa, obter_num_int_positivo

def main():
    menu ='''
    a. Inserir produtos    (opção 1)
    b. Calcular conta      (opção 2)
    c. Imprimir conta      (opcao 3)
    e. Confirmar pagamento (opcao 4)'''

    print(menu)
    funcoes_menu()

def funcoes_menu():
    opcao = obter_num_int_in_faixa('Opção: ', 1, 4)
    total_conta = 0
    agua = 0
    cerveja = 0
    tira_gosto = 0
    while True:
        if opcao == 1:
            print('\n Cerveja (C) - R$ 9.0\n Tira-Gosto (T) - R$ 39.0\n Água (A) - R$ 5.0\n Sair -> digite 0 0')

            pedido = obter_texto('Seu pedido: ')
            if pedido == '0':
                ...
            else:
                tipo = pedido.split() [1]

                while tipo != '0':
                    qtd_produto = int(pedido.split() [0])
                    tipo = pedido.split() [1]

                    if tipo == 'A' or tipo == 'a':
                        agua += qtd_produto
                    elif tipo == 'C' or tipo == 'c':
                        cerveja += qtd_produto
                    elif tipo == 'T' or tipo == 't':
                        tira_gosto += qtd_produto
                    
                    pedido = obter_texto('Seu pedido: ')
                    if pedido == '0':
                        break
            print('')
            opcao = obter_num_int_in_faixa('Opção: ', 1, 4)

        elif opcao == 2:
            valor_bruto = agua*5 + cerveja*9 + tira_gosto*39
            taxa_servico = (10/100)*valor_bruto
            valor_taxado = valor_bruto + taxa_servico

            if cerveja >= 10 or valor_bruto > 200:
                total_conta = valor_bruto
                situacao_taxa = 'Isento de taxa'
            else:
                total_conta = valor_taxado
                situacao_taxa = 'Taxado'
            print(f'Conta calculada!\n')
            opcao = obter_num_int_in_faixa('Opção: ', 1, 4)

        elif opcao == 3:
            qtd_pagantes = obter_num_int_positivo('Quantidade de pagantes: ')

            valor_individual = total_conta/qtd_pagantes

            print(f'''
    Valor conta: R$ {valor_bruto}
    Valor Individual: R$ {valor_individual:.2f}
    Taxa de serviço: R$ {taxa_servico} - {situacao_taxa}
    VALOR TOTAL: R$ {total_conta:.2f}''')
            
            opcao = obter_num_int_in_faixa('Opção: ', 1, 4)
        elif opcao == 4:
            print(' --> Pagamento confirmado! Conta da mesa encerrada!\n')
            entrada = obter_num_int_in_faixa('Calcular outra comanda? 1 - Sim / 2 - Não ', 1, 2)
            if entrada == 1:
                total_conta = 0
                agua = 0
                cerveja = 0
                tira_gosto = 0
                opcao = obter_num_int_in_faixa('Opção: ', 1, 4)
            else:
                print('bye bye ;)')
                break


def obter_texto(label):
    entrada = input(label)
    
    if entrada == '0':
        return entrada
    
    tipo = entrada.split() [1]
    
    if tipo in ['A', 'a', 'C', 'c', 'T', 't']:
        return entrada
    elif entrada != 0 or tipo not in ['A', 'a', 'C', 'c', 'T', 't']:
        print('Opção inválida. Tente novamente!')
        return obter_texto(label)


main()