from funcoes_uteis_copy1 import ler_num_int_min, limpar_tela
import time

def main():
    lista = '''
    ---- PESQUISA DE PREÇOS ----
'''

    opcao = menu()
    qtd_produtos = 0
    soma_produtos = 0

    while opcao != sair:
        if opcao == adc_produto:
            qtd_produtos += 1

            descricao = str(input('Digite o nome do produto: '))
            especificacao = str(input('Digite a especificação do produto (Ex.: 2 kg): '))
            valor = str(input('Digite o valor do produto: '))
            soma_produtos += float(valor)

            lista += f'{qtd_produtos}- {descricao} ({especificacao})'.ljust(33) + f'R$ {float(valor):6.2f}\n'
            time.sleep(0.7)
            print('>> Produto adicionado!!')
            time.sleep(1)
            enter_to_continue()

            opcao = menu()

        elif opcao == mostrar_list:
            if soma_produtos == 0:
                print(lista)
                print('Nenhum produto incluído')
                print (f'{40*'-'}\n{'Valor total:'.ljust(33)}R$ {soma_produtos:6.2f}')
                print('')
                time.sleep(1.5)
            else:
                print(lista)
                print (f'{40*'-'}\n{'Valor total:'.ljust(33)}R$ {soma_produtos:6.2f}')
                time.sleep(1.5)
                print('')
            enter_to_continue()
            opcao = menu()            

        elif opcao == pagamento:
            if soma_produtos < 30:
                print(lista)
                print (f'{40*'-'}\n{'Valor total:'.ljust(33)}R$ {soma_produtos:6.2f}')
                print(formas_pagamento(soma_produtos))
                escolha = validar_opcao(2)
                if escolha == 1:
                    print(f'>> Pagamento a vista selecionado! Valor: R$ {soma_produtos}')
                    input('\n<Enter> para confirmar o pagamento..')
                    time.sleep(1)
                    print('Pagamento confirmado!')
                    return
                elif escolha == 2:
                    qtd_parcelas = ler_num_int_min('Digite a quantidade de parcelas: ', 2)
                    print(f'>> Pagamento parcelado: {qtd_parcelas}x de R$ {calcular_juros(soma_produtos, qtd_parcelas):.2f}')
                    input('\n<Enter> para confirmar o pagamento..')
                    time.sleep(1)
                    print('Pagamento confirmado!')
                    return

            else:
                print(lista)
                print (f'{40*'-'}\n{'Valor total:'.ljust(33)}R$ {soma_produtos:6.2f}')
                print('')
                time.sleep(1)
                print(formas_pagamento(soma_produtos))
                escolha = validar_opcao(3)
                if escolha == 1:
                    print(f'>> Pagamento a vista selecionado! Valor: R$ {soma_produtos}')
                    input('\n<Enter> para confirmar o pagamento..')
                    time.sleep(1)
                    print('Pagamento confirmado!')
                    return

                elif escolha == 2 and soma_produtos <= 100:
                    qtd_parcelas = ler_num_int_min('Digite a quantidade de parcelas: ', 2)
                    if qtd_parcelas > 3:
                        print(f'>> Pagamento parcelado com juros: {qtd_parcelas}x de R$ {calcular_juros(soma_produtos, qtd_parcelas):.2f}')
                    else:
                        print(f'>> Pagamento parcelado: {qtd_parcelas}x de R$ {(soma_produtos/qtd_parcelas):.2f}')
                    input('\n<Enter> para confirmar o pagamento..')
                    time.sleep(1)
                    print('Pagamento confirmado!')
                    return

                elif escolha == 2 and soma_produtos > 100:
                    qtd_parcelas = ler_num_int_min('Digite a quantidade de parcelas: ', 2)
                    while qtd_parcelas > 5:
                        print('Ops, nessa opção, o limite de parcelas é 5x. Tente novamente!')
                        qtd_parcelas = ler_num_int_min('Digite a quantidade de parcelas: ', 2)
                    print(f'>> Pagamento parcelado: {qtd_parcelas}x de R$ {(soma_produtos/qtd_parcelas):.2f}')
                    input('\n<Enter> para confirmar o pagamento..')
                    time.sleep(1)
                    print('Pagamento confirmado!')
                    return
                
                elif escolha == 3 and soma_produtos <= 100:
                    qtd_parcelas = ler_num_int_min('Digite a quantidade de parcelas: ', 4)
                    print(f'>> Pagamento parcelado: {qtd_parcelas}x de R$ {calcular_juros(soma_produtos, qtd_parcelas):.2f}')
                    input('\n<Enter> para confirmar o pagamento..')
                    time.sleep(1)
                    print('Pagamento confirmado!')
                    return
                
                elif escolha == 3 and soma_produtos > 100:
                    qtd_parcelas = ler_num_int_min('Digite a quantidade de parcelas: ', 6)
                    print(f'>> Pagamento parcelado: {qtd_parcelas}x de R$ {calcular_juros(soma_produtos, qtd_parcelas):.2f}')
                    input('\n<Enter> para confirmar o pagamento..')
                    time.sleep(1)
                    print('Pagamento confirmado!')
                    return
                

def validar_opcao(qtd_opcoes):
    escolha = ler_num_int_min('Digite a opção de pagamento: ', 1)
    while escolha > qtd_opcoes:
        print('Opção não cadastrada. Digite uma opção válida!')
        escolha = ler_num_int_min('Digite a opção de pagamento: ', 1)
    return escolha


def menu():
    print('''
    --- MENU DE OPÇÕES ---
    1 - Adicionar Item
    2 - Imprimir lista
    3 - Formas de pagamento
    0 - Sair''')
    opcao = ler_num_int_min('Digite o valor da opção desejada: ', 0)

    while opcao > 3:
        print('A opção digitada não é válida!')
        opcao = ler_num_int_min('Digite o valor da opção desejada', 0)
    return opcao


def formas_pagamento(soma_produtos):
    if soma_produtos < 30:
        valor_parcela = calcular_juros(soma_produtos, 6)
        return f'Formas de pagamento: \n1- À vista: R$ {soma_produtos:.2f};\n2- Parcelado em até 6x de R$ {valor_parcela:.2f} com taxa de juros compostos de 5% a.m'
    elif soma_produtos <= 100:
        valor_parcela = soma_produtos/3
        valor_parcela_juros = calcular_juros(soma_produtos, 6)
        return f'Formas de pagamento: \n1- À vista: R$ {soma_produtos:.2f}\n2- Parcelado em até 3x de R$ {valor_parcela:.2f} sem juros\n3- Parcelado em até 6x de R$ {valor_parcela_juros:.2f} com taxa de juros compostos de 5% a.m'
    elif soma_produtos > 100:
        valor_parcela = soma_produtos/5
        valor_parcela_juros = calcular_juros(soma_produtos, 6)
        return f'Formas de pagamento: \n1- À vista: R$ {soma_produtos:.2f};\n2- Parcelado em até 5x de R$ {valor_parcela:.2f} sem juros\n3- Parcelado em até 6x de R$ {valor_parcela_juros:.2f} com taxa de juros compostos de 5% a.m'


def calcular_juros(soma_produtos, qtd_parcelas):
    valor_parcela = soma_produtos * (0.05*(1+0.05)**qtd_parcelas) / ((1+0.05)**qtd_parcelas -1)
    return valor_parcela


def enter_to_continue():
    input('<Enter> to continue..')
    limpar_tela()

sair = 0
adc_produto = 1
mostrar_list = 2
pagamento = 3


main()
        