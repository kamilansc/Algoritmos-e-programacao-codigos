# Escreva um programa que calcule o Índice de Massa Corporal (IMC), dado o peso e a altura.
# Entrada   Saída Esperada
# 70 1.75       22.86
# 90 1.80       27.78
# 50 1.60       19.53

# Entrada
peso = float(input("Digite o peso em quilogramas: "))
altura = float(input("Digite a altura em metros: "))

# Processamento
imc = peso / (altura)**2

# Saída
print(f"----> O IMC dado peso e altura é {imc:.2f} kg/m².")