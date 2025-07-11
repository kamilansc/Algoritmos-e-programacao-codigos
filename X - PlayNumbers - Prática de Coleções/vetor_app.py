from funcoes_genericas import *

def main():
    menu = '''\n\t>>> Bem vindo ao PlayNumbers !!! <<<
    1 - Inicializar Colecão Numérica
    2 - Mostrar todos os valores
    3 - Resetar coleção
    4 - Mostrar quantidade de itens na coleção
    5 - Mostrar maior e menor valor (e suas posições)
    6 - Somatório dos valores
    7 - Média dos valores
    8 - Mostrar valores positivos e quantidade
    9 - Mostrar valores negativos e quantidade
    10 - Atualizar valores por alguma regra escolhida
    11 - Adicionar novos valores
    12 - Remover item por valor exato
    13 - Remover item por posição
    14 - Modificar valor específico por posição
    15 - Salvar valores em arquivo
    
    0 - Sair
    Opção: '''

    opcao = int(input(menu))

    colecao = []
    while opcao != 0:
        if opcao == 1:
            tipo_colecao = int(input('''
>>> Escolha como você deseja gerar o conjunto de valores:
    1 - Gerar valores automaticamente
    2 - Informar valores
    3 - Carregar valores de um arquivo
    Opção: '''))
            print('')

            if tipo_colecao == 1:
                inicializar_vetor_com_valores_automaticos(colecao)
                
            elif tipo_colecao == 2:
                inicializar_vetor_com_valores_do_usuario(colecao)

            elif tipo_colecao == 3:
                nome_arquivo = input('Qual o nome do arquivo (adicione .txt ao final)? ')
                carregar_valores_do_arquivo(colecao, nome_arquivo)

        elif opcao == 2:
            mostrar_todos_os_valores_da_colecao(colecao)

        elif opcao == 3:
            if not colecao:
                print('''
    *** Não há nenhuma coleção de valores armazenada. 
    *** Primeiramente, inicialize os valores na opção 1 do menu.''')
            else:
                valor_padrao = int(input('Digite um valor para substituir todos os atuais valores: '))
                colecao = resetar_valores_da_colecao(colecao, valor_padrao)
                print('>>> Sua coleção foi resetada com sucesso!! <<<')
        
        elif opcao == 4:
            print(mostrar_qtd_de_itens_na_colecao(colecao))

        elif opcao == 5:
            maior_valor, posicao_maior, menor_valor, posicao_menor  = mostrar_maior_e_menor_valor(colecao)
            print(f'\n\tMaior valor: {maior_valor} Posição: {posicao_maior}')
            print(f'\tMenor valor: {menor_valor} Posição: {posicao_menor}')
        
        elif opcao == 6:
            somatorio = mostrar_somatorio_dos_valores(colecao)
            print(f'\n\t>> Somatório da sua coleção atual: {somatorio} <<')
        
        elif opcao == 7:
            media = mostrar_media_dos_valores(colecao)
            print(f'\n\t>> Média da sua coleção atual: {media:.1f}')
        
        elif opcao == 8:
            valores_positivos, quantidade = mostrar_valores_positivos_e_qtd(colecao)
            print(f'\n>> Na sua coleção há {quantidade} valor(es) positivo(s)!')
            print(f'\n{10*'-'} Valores positivos {10*'-'}')
            print(' | '.join(str(item) for item in valores_positivos))

        elif opcao == 9:
            valores_negativos, quantidade = mostrar_valores_negativos_e_qtd(colecao)
            print(f'\n>> Na sua coleção há {quantidade} valor(es) negativo(s)!')
            print(f'\n{10*'-'} Valores negativos {10*'-'}')
            print(' | '.join(str(item) for item in valores_negativos))

        elif opcao == 10:
            submenu = '''
    Ok! Agora, escolha uma das regras abaixo:
    1. Multiplicar por um valor
    2. Elevar a um valor (exponenciação)
    3. Reduzir a uma fração
    4. Substituir valores negativos por um número aleatórios de uma faixa
    5. Ordenar valores
    6. Embaralhar valores
    Opção: '''
            
            escolha = int(input(submenu))
            atualizar_valor_via_regra(colecao, escolha)

        elif opcao == 11:
            adicionar_novos_valores(colecao)

        elif opcao == 12:
            colecao = remover_itens_por_valor_exato(colecao)

        elif opcao == 13:
            remover_item_por_posicao(colecao)
        
        elif opcao == 14:
            modificar_valor_por_posicao(colecao)

        elif opcao == 15:
            nome_arquivo = input('Nome do arquivo: ')
            salvar_dados_em_arquivo(colecao, nome_arquivo)

        opcao = int(input(menu))

    salvar_dados_em_arquivo(colecao, 'arq_padrao_dados_playnumbers01.txt')



main()