# ATIVIDADE DO CAPÍTULO 9 (ESTUDO DE CASO: JOGO DE PALAVRAS) DO LIVRO PENSE EM PYTHON
# ASSUNTO: MANIPULAÇÃO DE STRINGS

from uteis_str import contem_caractere, avoids, uses_only, uses_all, is_abecedarian

def main():
    menu = '''
    >>>> WordPLAY <<<<
    1 - Palavras com Tamanho N+ (9.1)
    2 - Palavras sem o Caractere Proibido (9.2)
    3 - Palavras que evitam Letras Proibidas (9.3)
    4 - Palavras que contém apenas letras permitidas (9.4)
    5 - Palavras que só contém letras obrigatórias (9.5)
    6 - Palavras em que as letras são em ordem alfabética (9.6)

    0 - Sair
    >>>> '''
    opcao = int(input(menu))
    while opcao != 0:
        if opcao == 1:
            mostrar_palavras_pelo_tamanho()
        elif opcao == 2:
            mostrar_palavras_sem_caracter_proibido()
        elif opcao == 3:
            mostrar_palavras_sem_letras_proibidas()
        elif opcao == 4:
            letras_permitidas = input('Letras permitidas: ')
            mostrar_palavras_apenas_com_letras_permitidas(letras_permitidas)
        elif opcao == 5:
            letras_obrigatorias = input('Letras obrigatórias: ')
            mostrar_palavras_que_so_contem_letras_obrigatorias(letras_obrigatorias)
        elif opcao == 6:
            mostrar_palavras_com_letras_em_ordem_alfabetica()
        
        
        opcao = int(input(menu))


def mostrar_palavras_pelo_tamanho():
    tamanho = int(input('Digite o tamanho mínimo desejado das palavras: '))
    arquivo = open('br-sem-acentos.txt')
    contador = 0
    contador_filtro = 0
    for linha in arquivo:
        palavra = linha.strip()
        contador += 1
        if len(palavra) >= tamanho:
            print(2*' ', palavra)
            contador_filtro += 1
    
    mostrar_dados_descritivos(contador_filtro, contador)


def mostrar_palavras_sem_caracter_proibido():
    contador = 0
    contador_filtro = 0
    arquivo = open('br-sem-acentos.txt')
    caractere_proibido = input('Caractere proibido: ')
    for linha in arquivo:
        palavra = linha.strip()
        contador += 1
        if not contem_caractere(palavra, caractere_proibido):
            print(palavra)
            contador_filtro += 1
    
    mostrar_dados_descritivos(contador_filtro, contador)


def mostrar_palavras_sem_letras_proibidas():
    contador = 0
    contador_filtro = 0
    arquivo = open('br-sem-acentos.txt')
    letras_proibidas = input('Letras proibidas: ')
    for linha in arquivo:
        palavra = (linha.strip()).lower()
        contador += 1
        if avoids(palavra, letras_proibidas):
            print(palavra)
            contador_filtro += 1

    mostrar_dados_descritivos(contador_filtro, contador)


def mostrar_palavras_apenas_com_letras_permitidas(letras_permitidas):
    contador = 0
    contador_filtro = 0
    arquivo = open('br-sem-acentos.txt')
    for linha in arquivo:
        palavra = (linha.strip()).lower()
        contador += 1
        if uses_only(palavra, letras_permitidas):
            print(palavra)
            contador_filtro += 1
    
    mostrar_dados_descritivos(contador_filtro, contador)


def mostrar_palavras_que_so_contem_letras_obrigatorias(letras_obrigatorias):
    contador = 0
    contador_filtro = 0
    arquivo = open('br-sem-acentos.txt')
    for linha in arquivo:
        palavra = (linha.strip()).lower()
        contador += 1
        if uses_all(palavra, letras_obrigatorias):
            print(palavra)
            contador_filtro += 1

    mostrar_dados_descritivos(contador_filtro, contador)


def mostrar_palavras_com_letras_em_ordem_alfabetica():
    contador = 0
    contador_filtro = 0
    arquivo = open('br-sem-acentos.txt')
    for linha in arquivo:
        palavra = linha.strip().lower()
        contador += 1
        if is_abecedarian(palavra):
            print(palavra)
            contador_filtro += 1
    
    mostrar_dados_descritivos(contador_filtro, contador)


# Customização
def mostrar_dados_descritivos(contador_filtro, contador_total):
    percentual = (contador_filtro/contador_total)*100
    print(f'''
    Qtd total de palavras: {contador_total}
    Qtd palavras filtradas: {contador_filtro}
    Porcentagem (filtradas/total): {percentual:.3f}%''')


main()