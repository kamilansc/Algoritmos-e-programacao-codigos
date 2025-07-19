from fmr_funcoes import mapear, separar_em_dicionarios
import funcoes_validacao as fv
import funcionalidades_funcoes as ff

def main():
    resultados_escolas = load_resultados_escolas()

    menu = '''|>>> RESULTADO DAS ESCOLAS NO ENEM 2024 <<<|
    1 - Top N Brasil (todas as áreas)
    
    Opção: '''

    saida = 'Opção inválida. Tente novamente!'
    opcao = fv.obter_num_int_faixa(menu, 0, 1, saida)
    
    while opcao != 0:
        if opcao == 1:
            ff.rankear_resultados_pela_media(resultados_escolas)


def load_resultados_escolas():
    colecao = mapear(open('enem2014_teste.txt'), lambda x:x.strip())
    mapear(colecao, separar_em_dicionarios)


load_resultados_escolas()