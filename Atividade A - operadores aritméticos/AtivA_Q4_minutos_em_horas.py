# Escreva um programa que converta minutos para horas e minutos.
# Entrada       Saída Esperada
# 125       2 hora(s) e 5 minuto(s)
# 90       1 hora(s) e 30 minuto(s)
# 200       3 hora(s) e 20 minuto(s)

# Entrada
print (">>> Conversão de minutos para horas e minutos <<<")
print("")
valor_total_minutos = int(input("Digite o valor em minutos: "))

# Processamento
# 1h = 60min
horas = valor_total_minutos // 60
minutos = valor_total_minutos % 60

# Saída
print (f"---> {valor_total_minutos} minutos equivalem à {horas}h{minutos}min")
