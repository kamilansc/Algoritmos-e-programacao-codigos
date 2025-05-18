# Escreva um programa que aplique um desconto percentual sobre um preço inicial.
# Entrada Saída Esperada
#   100 10     90.0
#   200 25     150.0
#   500 5      475.0

# Entrada
valor_produto = float(input("Digite o valor do produto: "))
desconto_percentual = int(input("Digite o valor percentual a ser descontado: "))

# Processamento
novo_valor = valor_produto - (valor_produto * (desconto_percentual/100))

# Saída
print(f"O novo valor com desconto de {desconto_percentual}% aplicado é R${novo_valor:.2f} !!")
