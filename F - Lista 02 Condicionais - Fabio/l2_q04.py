from funcoes_uteis import receber_resposta


# 4. Leia 1 (um) número de 2 (dois) dígitos, verifique e escreva se o algarismo da dezena é igual ou diferente do algarismo da unidade.



def main():
    label = 'Digite um número de dois dígitos: '
    numero = int(receber_resposta(label))

    dezena = numero // 10
    unidade = numero % 10
    print(f'Dezena: {dezena} Unidade: {unidade}')
    
    if dezena == unidade:
        print(f'O número {numero} possui o mesmo algarismo na dezena e na unidade.')
    else:
        print('A dezena e a unidade são diferentes.')


main()