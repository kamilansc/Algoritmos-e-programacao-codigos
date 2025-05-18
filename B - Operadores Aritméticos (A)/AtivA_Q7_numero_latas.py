# Escreva um programa que calcule quantas latas de tinta são necessárias para pintar uma área.
# Entrada   Saída Esperada
#   100         20 5
#   50          10 5
#   75          25 3

# Entrada
altura = float(input("Digite o valor da altura: "))
comprimento = float(input("Digite o valor do comprimento: "))
rendimento = float(input("Digite o rendimento da lata de tinta: "))

# Processamento
area = altura*comprimento
qntd_latas = area/rendimento

# Saída
print(f"O valor da área é {area} e será necessário {qntd_latas} lata(s)!!")