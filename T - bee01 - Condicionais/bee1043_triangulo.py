def main():
    entrada = obter_num_real()
    lado_a = entrada[0]
    lado_b = entrada[1]
    lado_c = entrada[2]
    
    if lado_a+lado_b > lado_c and lado_a+lado_c > lado_b and lado_b+lado_c > lado_a:
        print(f'Perimetro = {(lado_a + lado_b + lado_c):.1f}')
    else:
        print(f'Area = {((lado_a + lado_b)*lado_c/2):.1f}')


def obter_num_real():
    numeros = input().split()

    try:
        num1 = float(numeros[0])
        num2 = float(numeros[1])
        num3 = float(numeros[2])
        return num1, num2, num3
    except:
        return obter_num_real()


main()