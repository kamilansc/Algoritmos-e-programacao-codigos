# 5. Leia um número inteiro (3 dígitos), calcule e escreva a soma de seus elementos (C + D + U).

# Entrada
numero = int(input('Digite um número inteiro de 3 dígitos: '))

# Processamento
centena = numero // 100
dezena = (numero % 100) // 10
unidade = (numero % 100) % 10

soma_numero = centena + dezena + unidade

# Saída
print(f'A soma dos algarismos do número {numero} é igual a {soma_numero}.')