from funcoes_uteis_copy3 import ler_num_int_positivo

def main():
    n = ler_num_int_positivo('Quantidade de termos da sequência para exibir: ')

    termo = 1
    variavel_soma = 2
    sequencia = []

    for i in range(1, n + 1, 1):
#       print(termo, end=" ")
        sequencia.append(str(termo))
        termo += variavel_soma
        
        variavel_soma += 1
    
    print(', '.join(sequencia))


main()