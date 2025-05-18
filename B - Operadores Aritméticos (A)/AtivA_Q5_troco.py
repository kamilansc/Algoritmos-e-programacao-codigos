# Escreva um programa que determine a quantidade de notas de 50 e 10 necessárias para um determinado valor.
# Entrada       Saída Esperada
#   130     2 nota(s) de 50 e 3 nota(s) de 10
#   70      1 nota(s) de 50 e 2 nota(s) de 10
#   90      1 nota(s) de 50 e 4 nota(s) de 10

# Entrada
valor = int(input("Digite o valor: "))

# Processamento
qntd_notas_cinquenta = valor // 50
qntd_notas_dez = (valor - qntd_notas_cinquenta*50) // 10
sobra = (valor - qntd_notas_cinquenta*50) % 10
# Saída
print(f"---> Serão necessárias {qntd_notas_cinquenta} notas de 50 e {qntd_notas_dez} notas de 10 e sobrará R${sobra:.1f}!!")