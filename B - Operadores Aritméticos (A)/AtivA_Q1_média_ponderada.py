#Escreva um programa que calcule a média ponderada de três notas, considerando seus 
# respectivos pesos.
# Entrada           Saída Esperada
# 8 2 7 3 6 5           6.7
# 10 4 5 2 8 4          8.2
# 3 1 7 1 10 2          7.5

# Entrada
nota_1 = float(input("Digite a nota 1: "))
peso_1 = int(input ("Digite o peso da nota 1: "))
nota_2 = float(input("Digite a nota 2: "))
peso_2 = int(input ("Digite o peso da nota 2: "))   
nota_3 = float(input("Digite a nota 3: "))
peso_3 = int(input ("Digite o peso da nota 3: "))

# Processamento
media_ponderada = (nota_1*peso_1 + nota_2*peso_2 + nota_3*peso_3) / (peso_1+peso_2+peso_3)

# Saída
print (f"Média ponderada das notas {nota_1}, {nota_2} e {nota_3}: {media_ponderada:.1f} !!")