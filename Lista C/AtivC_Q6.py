# 6. Leia uma velocidade em km/h, calcule e escreva esta velocidade em m/s. (Vm/s = Vkm/h / 3.6)

# Entrada
velocidade_quilometros = int(input('Digite o valor da velocidade em km/h: '))

# Processamento
velocidade_metros_segundos = velocidade_quilometros / 3.6

# Saída
print(f'A velocidade de {velocidade_quilometros}km/h é equivalente a {velocidade_metros_segundos}m/s!!')