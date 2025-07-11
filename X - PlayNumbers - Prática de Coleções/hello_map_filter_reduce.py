def main():
    valores = mapear(input().split(), int)

    valores_positivos = filtrar(valores, eh_positivo)
    valores_negativos = filtrar(valores, eh_negativo)

    somatorio_positivos = reduzir(valores_positivos, somar, 0)
    somatorio_negativos = reduzir(valores_negativos, somar, 0)

    soma_pares = reduzir(filtrar(valores, eh_par), somar, 0)
    soma_impares = reduzir(filtrar(valores, eh_impar), somar, 0)

    produto_positivos = reduzir(valores_positivos, multiplicar, 1)
    produto_negativos = reduzir(valores_negativos, multiplicar, 1)

    maior_valor = reduzir(valores, eh_maior, valores[0])

    type_valores = ''
    for valor in valores:
        type_valores += str(type(valor))
    
    print(f'{valores}\n{type_valores}')

    print(f'Valores positivos: {valores_positivos}')
    print(f'Valores negativos: {valores_negativos}')

    print(f'Somatório Positivos: {somatorio_positivos}')
    print(f'Somatório Negativos: {somatorio_negativos}')

    print(f'Soma dos Pares: {soma_pares}')
    print(f'Soma dos Ímpares: {soma_impares}')

    print(f'Produto dos Positivos: {produto_positivos}')
    print(f'Produto dos Negativos: {produto_negativos}')

    print(f'Maior valor: {maior_valor}')

def mapear(colecao, funcao_transformadora):
    nova_colecao = []

    for item in colecao:
        nova_colecao.append(funcao_transformadora(item))

    return nova_colecao


def filtrar(colecao, criterio):
    nova_colecao = []

    for item in colecao:
        if criterio(item):
            nova_colecao.append(item)

    return nova_colecao


def reduzir(colecao, funcao_redutora, inicial):
    acumulado = inicial

    for item in colecao:
        acumulado = funcao_redutora(acumulado, item)
    
    return acumulado


# funções auxiliares (booleanas) da função FILTRAR
def eh_positivo(valor):
    return valor > 0


def eh_negativo(valor):
    return valor < 0


def somar(valor1, valor2):
    return valor1 + valor2


def eh_par(valor):
    return valor % 2 == 0


def eh_impar(valor):
    return not eh_par(valor)


def eh_maior(valor1, valor2):
    return valor1 if valor1 > valor2 else valor2


def eh_menor(valor1, valor2):
    return valor1 if valor1 < valor2 else valor2


def multiplicar(valor1, valor2):
    return valor1 * valor2


if __name__ == '__main__':
    main()