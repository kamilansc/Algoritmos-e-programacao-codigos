def contem_caractere(palavra, caractere):
    for letra in palavra:
        if letra == caractere:
            return True
    return False


def avoids(palavra, letras_proibidas):
    for letra in palavra:
        if contem_caractere(letras_proibidas, letra):
            return False
    return True


def uses_all(palavra, letras_permitidas):
    for letra in palavra:
        if avoids(letra, letras_permitidas):
            return False
    return True
