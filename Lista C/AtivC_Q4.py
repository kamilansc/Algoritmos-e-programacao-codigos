# 04. Leia o valor do dólar e um valor em dólar, calcule e escreva o equivalente em real (R$) 

# Entrada 
valor_dolar = float(input('Digite o valor do dólar hoje: '))
dolar = float(input('Digite o valor em Dólar para conversão: '))

#Processamento
reais = dolar * valor_dolar

# Saída 
print(f'{dolar} dólares equivalem a R${reais:.2f}!!')