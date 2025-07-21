from fmr_funcoes import mapear, separar_em_dicionarios
import funcoes_validacao as fv
import funcionalidades_funcoes as ff

def main():
    resultados_escolas = load_resultados_escolas()

    menu = '''|>>> RESULTADO DAS ESCOLAS NO ENEM 2024 <<<|
    1 - Top N Brasil (todas as áreas)
    2 - Top N Brasil por ÁREA
    3 - Top N por ESTADO
    4 - Top N por ESTADO e REDE
    5 - Média nacional por ÁREA
    6 - Melhor escola de ÁREA por ESTADO ou BR
    7 - Lista escolas por ESTADO ordenadas por RENDA
    8 - Busca escola específica por NOME
    9 - Ranking ENEM por ESTADO
    10 - Ranking ENEM por REGIÃO do país

    0 - Sair
    
    Opção: '''

    saida = 'Opção inválida. Tente novamente!'
    opcao = fv.obter_num_int_faixa(menu, 0, 10, saida)
    
    while opcao != 0:
        if opcao == 1:
            tamanho_ranking = fv.obter_num_int_positivo('Digite o tamanho do ranking desejado: ')
            top_n_escolas = ff.rankear_resultados_pela_media(resultados_escolas, tamanho_ranking)
            print(*top_n_escolas, sep='\n\n')
            print('')
            # * -> desempacota lista e separa com base no sep 
        
        elif opcao == 2:
            tamanho_ranking = fv.obter_num_int_positivo('Digite o tamanho do ranking desejado: ')
            escolha_area = ff.mostrar_menu_areas()
            top_n_escolas_area = ff.rankear_resultados_pela_area(resultados_escolas, tamanho_ranking, escolha_area)
            print(*top_n_escolas_area, sep='\n\n')
            print('')
        
        elif opcao == 3:
            tamanho_ranking = fv.obter_num_int_positivo('Digite o tamanho do ranking desejado: ')
            escolha_estado = ff.verificar_estado()
            top_n_escolas_estado = ff.rankear_resultados_pelo_estado(resultados_escolas, tamanho_ranking, escolha_estado)
            print(*top_n_escolas_estado, sep='\n\n')
            print('')

        elif opcao == 4:
            tamanho_ranking = fv.obter_num_int_positivo('Digite o tamanho do ranking desejado: ')
            escolha_estado = ff.verificar_estado()
            escolha_rede = ff.verificar_rede()
            top_n_escolas_estado_rede = ff.rankear_resultados_pela_estado_rede(resultados_escolas, tamanho_ranking, escolha_estado, escolha_rede)
            print(*top_n_escolas_estado_rede, sep='\n\n')
            print('')

        elif opcao == 5:
            escolha_area = ff.mostrar_menu_areas()
            media_nacional = ff.calcular_media_nacional_area(resultados_escolas, escolha_area)
            print(f'\n\t>>> A média nacional em {escolha_area.upper()} é {media_nacional:.1f}\n')

        elif opcao == 6:
            escolha_area = ff.mostrar_menu_areas()
            saida = 'Essa opção não está cadastrada. Digite uma opção válida!'
            escolha_dimensao = fv.obter_num_int_faixa('Digite o valor de uma opção (1 - estado | 2 - Brasil): ',\
            1, 2, saida)

            if escolha_dimensao == 1:
                escolha_estado = ff.verificar_estado()
                melhor_escola = ff.identificar_melhor_escola_de_area_por_estado(resultados_escolas, escolha_area, escolha_estado)
                print(f'\nA melhor escolha do estado de uf {escolha_estado} é \n{melhor_escola}.\n')

            else:
                melhor_escola = ff.rankear_resultados_pela_area(resultados_escolas, 1, escolha_area)
                print(f'Escola com melhor pontuação na área de {escolha_area}:', *melhor_escola, sep='\n')
                print('')
        
        elif opcao == 7:
            estado = ff.verificar_estado()
            lista_escolas = ff.mostrar_escolas_por_renda_e_estado(resultados_escolas, estado)

            if not lista_escolas:
                print('Nenhuma escola encontrada para os critérios especificados')
            else:
                print(*lista_escolas, sep='\n\n')
        
        elif opcao == 8:
            escola = ff.procurar_escola_por_nome(resultados_escolas)
            if not escola:
                print('Escola não encontrada!')
            else:
                print(f'Escola {escola[0].get('nome')}:', *escola, sep='\n')
                print('')
        
        elif opcao ==  9:
            estado = ff.verificar_estado()
            ranking_estadual = ff.mostrar_ranking_por_estado(resultados_escolas, estado)
            print(*ranking_estadual, sep='\n\n')

        elif opcao == 10:
            estados_regiao = ff.verificar_regiao()
            ranking_regional = ff.mostrar_ranking_por_regiao(resultados_escolas, estados_regiao)
            print(*ranking_regional, sep='\n\n')

        opcao = fv.obter_num_int_faixa(menu, 0, 10, saida)


def load_resultados_escolas():
    colecao = mapear(open('enem2014_nota_por_escola.txt'), lambda x:x.strip())
    nova_colecao = mapear(colecao, separar_em_dicionarios)

    return nova_colecao


main()