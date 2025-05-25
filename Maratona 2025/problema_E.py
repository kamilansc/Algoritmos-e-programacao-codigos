k = int(input())
y = int(input())
x_posicao = 1

antigo_divisor_comum = 0
atual_divisor_comum = 0
contador = 1
while k > 0:
    while contador < y:
        if y % contador == 0 and x_posicao % contador == 0:
            atual_divisor_comum = contador
        
        if atual_divisor_comum > antigo_divisor_comum:
            max_divisor_comum = atual_divisor_comum
        elif antigo_divisor_comum < atual_divisor_comum:
            max_divisor_comum = antigo_divisor_comum
            
        antigo_divisor_comum = atual_divisor_comum
        contador += 1
        '''divisor = 1
            x = 2
            divisor = 2
            x = 4
            divisor = 4'''
    x_posicao += max_divisor_comum
    k -= 1

print(x_posicao)

