# 8. Leia 2 números, calcule e escreva a divisão da soma pela subtração dos números lidos.

# Entrada
numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite um número: '))

# Processamento
divisao = (numero_1 + numero_2) / (numero_1 - numero_2)

# Saída
print(f'A divisão da soma pela subtração é {divisao}')