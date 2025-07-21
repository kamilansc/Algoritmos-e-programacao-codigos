def main():
    valor1, valor2 = input().split()

    while int(valor1) and int(valor2) not in [0]:
        lista_valores2 = []
        for algarismo in valor2:
            lista_valores2.append(algarismo)

        lista_valor_modificado = filter(lista_valores2, lambda x:x != valor1)
        
        if not lista_valor_modificado:
            lista_valor_modificado.append('0')
        
        valor_modificado = int(''.join(lista_valor_modificado))
        print(lista_valores2, valor1)
        print(valor_modificado)

        valor1, valor2 = input().split()


def filter(colecao, funcao_criterio):
    nova_colecao = []

    for item in colecao:
        if funcao_criterio(item):
            nova_colecao.append(item)
    
    return nova_colecao


main()