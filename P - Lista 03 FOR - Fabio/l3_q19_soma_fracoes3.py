from funcoes_uteis_copy3 import ler_num_int_positivo

def main():
    n = ler_num_int_positivo('Número: ')

    decrescente = 0
    sequencia = []
    soma = 0

    for numerador in range(1, n + 1, 1):
        denominador = n - decrescente
        if eh_impar(numerador):
            fracao = numerador/denominador
            soma += fracao

            if decrescente == 0:
                sequencia.append(f'{numerador}/{n}')
            else:
                sequencia.append(f'{numerador}/{denominador}')
        else:
            sinal = '-'
            fracao = -(denominador/numerador)
            soma += fracao

            sequencia.append(f'{sinal} {denominador}/{numerador}')
        
        decrescente += 1

    print(f'Frações somadas:  {" + ".join(sequencia).replace("+ -", "-")}')
    print(f'Resultado da soma: S = {soma:.2f}')


def eh_impar(num):
    return num % 2 != 0


main()