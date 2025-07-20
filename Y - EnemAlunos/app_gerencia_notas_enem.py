from fmr_funcoes import mapear, separar_em_dicionarios
import funcoes_validacao as fv
import funcionalidades_funcoes as ff

def main():
    resultados_escolas = load_resultados_escolas()

    menu = '''|>>> RESULTADO DAS ESCOLAS NO ENEM 2024 <<<|
    1 - Top N Brasil (todas as áreas)
    2 - Top N Brasil por Área
    3 - Top N por estado
    4 - Top N por estado e rede
    5 - Média nacional por Área
    
    Opção: '''

    saida = 'Opção inválida. Tente novamente!'
    opcao = fv.obter_num_int_faixa(menu, 0, 5, saida)
    
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

        opcao = fv.obter_num_int_faixa(menu, 0, 5, saida)


def load_resultados_escolas():
    colecao = mapear(open('enem2014_nota_por_escola.txt'), lambda x:x.strip())
    nova_colecao = mapear(colecao, separar_em_dicionarios)

    return nova_colecao


main()