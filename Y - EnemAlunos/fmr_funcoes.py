def mapear(colecao, funcao_modificadora):
    colecao_modificada = []

    for item in colecao:
        item_modificado = funcao_modificadora(item)
        colecao_modificada.append(item_modificado)
    
    return colecao_modificada


def filter(colecao, criterio):
    nova_colecao = []
    for item in colecao:
        if criterio(item):
            nova_colecao.append(item)
    
    return nova_colecao


def reduce(colecao, funcao_redutora, inicial):
    acumulado = inicial

    for item in colecao:
        acumulado = funcao_redutora(acumulado, item)

    return acumulado


def somar(valor1, valor2):
    return valor1 + valor2


def separar_em_dicionarios(item):
    dados_escola = item.split(';')

    dados_escola = converter_num_para_string(dados_escola)

    escola = {}
    escola['ranking'] = dados_escola[0]
    escola['nome'] = dados_escola[1]
    escola['municipio'] = dados_escola[2]
    escola['uf'] = dados_escola[3]
    escola['rede'] = dados_escola[4]
    escola['permanencia'] = dados_escola[5]
    escola['nivel_socioeconomico'] = dados_escola[6]
    escola['media_objetivas'] = dados_escola[7]
    escola['linguagens'] = dados_escola[8]
    escola['matematica'] = dados_escola[9]
    escola['ciencias_natureza'] = dados_escola[10]
    escola['humanas'] = dados_escola[11]
    escola['redacao'] = dados_escola[12]

    return escola


def converter_num_para_string(colecao):
    nova_colecao = []

    for item in range(len(colecao)):
        dado = colecao[item]

        if item >= 7:
            nova_colecao.append(float(dado.replace(',', '.')))
        else:
            nova_colecao.append(dado)
    
    return nova_colecao