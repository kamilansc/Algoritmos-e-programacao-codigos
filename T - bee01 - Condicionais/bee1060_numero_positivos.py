def main():
    contador_num_positivos = 0
    for num in range(1, 7):
        numero = float(input())
        while numero == 0:
            numero = float(input())
        
        if numero > 0:
            contador_num_positivos += 1
    
    print(f'{contador_num_positivos} valores positivos')
        

main()