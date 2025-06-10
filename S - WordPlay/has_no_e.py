def main():
    menu = '''
    >>>> WordPLAY <<<<
    1 - Palavras com Tamanho N+
    2 - Palavras sem o caractere proibido

    0 - Sair
    >>>> '''
    opcao = int(input(menu))
    while opcao != 0:
        if opcao == 1:
            tamanho = int(input('Digite o tamanho mínimo desejado das palavras: '))
            arquivo = open('br-sem-acentos.txt')
            for linha in arquivo:
                palavra = linha.strip()
                if len(palavra) >= tamanho:
                    print(2*' ', palavra)

        if opcao == 2:
            arquivo = open('br-sem-acentos.txt')
            caractere_proibido = input('\nCaractere proibido: ')
            contador_total = 0
            contador_filtro = 0
            for linha in arquivo:
                palavra = linha.strip()
                contador_total += 1
                if nao_tem_caractere(palavra, caractere_proibido) == True:
                    contador_filtro += 1
            
            mostrar_dados_descritivos(contador_filtro, contador_total)
        
        opcao = int(input(menu))


def nao_tem_caractere(palavra, caractere):
    for letra in palavra:
        if letra == caractere:
            return False
    return True


# Customização
def mostrar_dados_descritivos(contador_filtro, contador_total):
    percentual = (contador_filtro/contador_total)*100
    print(f'''
    Qtd total de palavras: {contador_total}
    Qtd palavras filtradas: {contador_filtro}
    Porcentagem (filtradas/total): {percentual:.1f}%''')


main()

