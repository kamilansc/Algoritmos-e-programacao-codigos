# 03 Leia um valor em minutos, calcule e escreva o equivalente em horas e minutos.

# Entrada
minutos = int(input('Digite o valor em minutos: '))

# Processamento 
horas = minutos // 60 
minutos_restantes = minutos % 60

# Saída
print(f'    {minutos} minutos equivalem a {horas}h{minutos_restantes}min!!')