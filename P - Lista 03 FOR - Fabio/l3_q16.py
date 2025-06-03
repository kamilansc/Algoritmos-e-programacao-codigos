from funcoes_uteis_copy3 import ler_num_int_min

def main():
    n = ler_num_int_min('\nQuantidade de termos da Sequencia de Fibonacci para exibir: ', 2)

    termo_anterior = 0
    termo_atual = 1
    sequencia = [str(termo_anterior), str(termo_atual)]

    for termo in range(2, n, 1):
        soma = termo_anterior + termo_atual 

        termo_anterior = termo_atual
        termo_atual = soma

        sequencia.append(str(termo_atual))

    print(', '.join(sequencia))

main()