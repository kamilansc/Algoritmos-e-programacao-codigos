# Escreva um programa que calcule a soma dos primeiros N números naturais.
# Entrada Saída Esperada
#   5          15
#  10          55
#  100        5050 

# Entrada
print("")
print (">>>>> Cálculo da soma dos números naturais partindo de x até y <<<<<")

limite_inferior = int(input("Digite o limite inferior da soma (Exemplo: se o limite é 1, então a soma incia a partir de 1): "))
limite_superior = int (input ("Digite o limite superior (Exemplo: se o limite é 5, então a soma termina no 5): "))

# Processamento
soma_par = limite_inferior + limite_superior
quantidade_par = (limite_superior - limite_inferior + 1) / 2
soma = soma_par*quantidade_par

# Saída
print ("")
print (f"A soma de {limite_inferior} à {limite_superior} é {soma:.0f}")