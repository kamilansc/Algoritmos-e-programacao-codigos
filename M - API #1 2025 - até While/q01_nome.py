from q4_text_utils import obter_texto

def main():
    nome_usuario = obter_texto('Nome do usuário: ')

    tamanho = len(nome_usuario)

    if tamanho % 2 == 0:
        mostrar_multiplos(tamanho)
    else:
        mostrar_divisores(tamanho)


def mostrar_multiplos(tamanho):
    contador = 0
    multiplo = tamanho
    print(f'Número par ==> Múltiplos de {tamanho}: ')
    while contador < tamanho:
        multiplo += tamanho
        print(multiplo)
        contador += 1


def mostrar_divisores(tamanho):
    contador = 1    
    print(f'Número ímpar ==> Divisores de {tamanho}: ')
    while contador <= tamanho:
        if tamanho % contador == 0:
            print(contador)
            contador += 1
        contador += 1


main()