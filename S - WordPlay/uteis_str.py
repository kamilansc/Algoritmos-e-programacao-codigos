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


def uses_only(palavra, letras_permitidas):
    for letra in palavra:
        if avoids(letra, letras_permitidas):
            return False
    return True


def uses_all(palavra, letras_obrigatorias):
    for letra in letras_obrigatorias:
        if not contem_caractere(palavra, letra):
            return False
    return True


def is_abecedarian(palavra):
    letra_anterior = ''
    for letra in palavra:
        if letra < letra_anterior:
            return False
        letra_anterior = letra


    return True


is_abecedarian('kamila')