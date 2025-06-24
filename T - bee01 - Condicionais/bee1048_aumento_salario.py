def main():
    salario = float(input())

    if salario > 0 and salario <= 400:
        valor_reajuste = 0.15*salario
        percentual = '15'
    elif salario <= 800:
        valor_reajuste = 0.12*salario
        percentual = '12'
    elif salario <= 1200:
        valor_reajuste = 0.1*salario
        percentual = '10'
    elif salario <= 2000:
        valor_reajuste = 0.07*salario
        percentual = '7'
    elif salario > 2000:
        valor_reajuste = 0.04*salario
        percentual = '4'
    
    print(f'Novo salario: {(salario + valor_reajuste):.2f}')
    print(f'Reajuste ganho: {valor_reajuste:.2f}')
    print(f'Em percentual: {percentual} %')


main()