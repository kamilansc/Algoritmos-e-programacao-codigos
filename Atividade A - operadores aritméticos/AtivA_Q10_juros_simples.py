# Escreva um programa que calcule o montante final em uma aplicação financeira com juros simples.
# Entrada           Saída Esperada
#   1000 0.02 6         1120.0
#   500 0.05 4          600.0
#   2000 0.01 12        2240.0

# Entrada
capital = float(input("Digite o valor do capital: "))
taxa_juros = float(input("Digite o valor da taxa: "))
tempo = float(input("Digite o valor do capital: "))

# Processamento
juros = capital * taxa_juros * tempo
montante = capital + juros

# Saída
print (f"O montante final dessa aplicação financeira é R$ {montante} !!")