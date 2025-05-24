def num_eh_perfeito():
    num = int(input('Digite um número inteiro mínimo: '))
    num_max = int(input('Digite um número inteiro máximo: '))

    num_atual = num

    while num_atual <= num_max:
        contador = 1
        soma_divisores = 0

        while contador < num_atual:
            if num_atual % contador == 0:
                soma_divisores += contador
                contador += 1 
            else:
                contador += 1

        if soma_divisores == num_atual:
            print (f' {num_atual} É PERFEITO')
        else:        
            print (f' {num_atual} NÃO É PERFEITO')

        num_atual += 1


num_eh_perfeito()