from funcoes_uteis_copy2 import obter_texto

def main():
    letra = obter_texto('Letra: ')
    print(eh_consoante_ou_vogal(letra))


def eh_consoante_ou_vogal(letra):
    if len(letra) != 1:
        print('Digite apenas UMA letra!')
        letra = obter_texto('Letra: ')
        return eh_consoante_ou_vogal(letra)

    vogais = 'aeiou'
    if letra.lower() in vogais:
        return ' >> É uma vogal!!'

    elif (letra.lower()).isalpha() and letra.lower() not in vogais:
        return ' >> É uma consoante!!'

    else:
        return ' >> Não é uma letra!!'


main()