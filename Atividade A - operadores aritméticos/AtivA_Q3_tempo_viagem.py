# Escreva um programa que calcule quanto tempo levará uma viagem, dado a distância e a velocidade média.

# Entrada   Saída Esperada
# 300 100       3.0
# 150 50        3.0
# 600 120       5.0

# Entrada
distancia = float(input("Digite a distância: "))
velocidade_media = float(input("Digite a velocidade média: "))

# Processamento
tempo = distancia / velocidade_media

# Saída
print(f"Tempo da viagem: {tempo:.0f}h")