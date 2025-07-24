from utils import obter_num_inteiro

def main():
    palavra = input('Digite a palavra que desejar criptografar: ')
    print(palavra)
    chave = obter_num_inteiro('Digite a chave C: ')
    nova_palavra = criptografar(palavra, chave)
    print(nova_palavra)


def criptografar(palavra, chave):
    vogais = ['a', 'e', 'i', 'o', 'u']
    consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    palavra_criptografada = ''

    for letra in palavra:
        letra_min = letra.lower()

        if letra_min in vogais:
            indice_criptografado = vogais.index(letra_min) + 1
            nova_letra = vogais[indice_criptografado % len(vogais)]

            # try:
            #     nova_letra = vogais[indice_criptografado]
            # except IndexError:
            #     nova_letra = vogais[indice_criptografado - len(vogais)]
        
        elif letra_min in consoantes:
            indice_criptografado = consoantes.index(letra_min) + 2*chave
            nova_letra = consoantes[indice_criptografado % len(consoantes)]

            # try:
            #     nova_letra = consoantes[indice_criptografado]
            # except IndexError:
            #     nova_letra = consoantes[indice_criptografado - len(consoantes)]
        
        else:
            nova_letra = letra
        
        if letra.isupper():
            nova_letra = nova_letra.upper()

        palavra_criptografada += nova_letra

    return palavra_criptografada
        

main()