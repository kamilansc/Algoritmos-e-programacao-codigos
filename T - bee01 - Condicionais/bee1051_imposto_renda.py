def main():
    salario = float(input())
    faixa_salario = salario - 2000

    if salario <= 2000:
        print('Isento')
        return
    elif salario <= 3000:
        valor_imposto = faixa_salario*0.08
    elif salario <= 4500:
        valor_imposto = 1000*0.08 + (faixa_salario-1000)*0.18
    elif salario > 4500:
        valor_imposto = (1000*0.08) + (1500*0.18) + (faixa_salario-2500)*0.28
    
    print(f'R$ {valor_imposto:.2f}')


main()