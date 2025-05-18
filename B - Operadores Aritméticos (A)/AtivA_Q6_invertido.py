# Escreva um programa que receba um número de três dígitos e exiba ele invertido.
# Entrada   Saída Esperada
#   123         321
#   450         54
#   987         789

# Entrada
numero = int(input("Digite o número a ser invertido: "))

# Processamento
centena = (numero % 100) % 10
dezena = (numero % 100) // 10
unidade = numero // 100

inverso = centena*100 + dezena*10 + unidade

# Saída
print(f"O número inverso de {numero} é {inverso} !!")
