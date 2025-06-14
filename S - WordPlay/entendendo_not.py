def main():
    entrada = input('Palavra: ')
    caracteres_testaveis = input('Caractere a ser verificado: ')
    if avoids(entrada, caracteres_testaveis):
        print(entrada)


def contem_caractere(palavra = k, caractere = k):
    for letra in palavra:
        if letra == caractere:
            return True
        
    return False


def avoids(palavra, letras_proibidas):
    for letra in palavra:
        if not contem_caractere(letras_proibidas, letra):
            return True
    return False


main()
