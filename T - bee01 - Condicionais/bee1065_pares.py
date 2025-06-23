def main():
    qtd_num_pares = 0
    for num in range (1, 6):
        numero = obter_num_int()
        if eh_par(numero):
            qtd_num_pares += 1
    
    print(f'{qtd_num_pares} valores pares')


def obter_num_int():
    entrada = input()

    try:
        return int(entrada)
    except:
        return obter_num_int()
    
    
def eh_par(num):
    return num % 2 == 0
main()