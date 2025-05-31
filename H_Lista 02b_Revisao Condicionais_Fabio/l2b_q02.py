from funcoes_uteis_copy2 import obter_texto

def main():
    letra = obter_texto('Letra: ')

    print(identificar_genero(letra))


def identificar_genero(letra):
    if letra.upper() == 'F':
        return 'Feminino'
    elif letra.upper() == 'M':
        return 'Masculino'
    else:
        return 'Sexo inválido'


main()