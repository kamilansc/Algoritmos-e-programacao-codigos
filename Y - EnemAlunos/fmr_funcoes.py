def mapear(colecao, funcao_modificadora):
    colecao_modificada = []

    for item in colecao:
        item_modificado = funcao_modificadora(item)
        colecao_modificada.append(item_modificado)
    
    return colecao_modificada


def separar_em_dicionarios(item):
    dados_escola = item.split(';')
    # for item in dados_escola
    # dados_escola = converter_num_para_string(dados_escola)
    mapear(dados_escola, lambda x:float(x.replace(',','.')))

    escola = {}

    escola['ranking'] = dados_escola[0]
    escola['nome'] = dados_escola[1]
    escola['municipio'] = dados_escola[2]
    escola['uf'] = dados_escola[3]
    escola['rede'] = dados_escola[4]
    escola['permanencia'] = dados_escola[5]
    escola['nivel_socioeconomico'] = dados_escola[6]
    escola['media_objetivas'] = float(dados_escola[7])
    escola['linguagens'] = float(dados_escola[8])
    escola['matematica'] = float(dados_escola[9])
    escola['ciencias_natureza'] = float(dados_escola[10])
    escola['humanas'] = float(dados_escola[11])
    escola['redacao'] = float(dados_escola[12])

    print(escola)
    return escola