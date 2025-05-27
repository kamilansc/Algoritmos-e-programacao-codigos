from q01_number_utils import obter_num_int_positivo

def main():
    x = obter_num_int_positivo('Número 1: ')
    y = obter_num_int_positivo('Número 2: ')
    
    print(encontrar_mdc(x, y))


def encontrar_mdc(x,y):
    if x < y:
        menor_num = x
    else:
        menor_num = y
    
    contador = 2
    novo_x = x
    novo_y = y
    while contador <= menor_num:
        while (novo_x % contador == 0) and (novo_y % contador == 0):
            divisor_comum = contador
            novo_x = novo_x/contador
            novo_y = novo_x/contador
            print(f'- {divisor_comum}')
        
        # if novo_x % contador == 0 or
        else:
            contador += 1
    return divisor_comum


'''def encontrar_mdc(x, y, contador = 1):
    if contador > x and contador > y:
        pass'''


main()