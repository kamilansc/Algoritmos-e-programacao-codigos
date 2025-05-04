# 14. Leia 3 notas de um aluno e o peso de cada nota, calcule e escreva a média ponderada.

# Entrada 
nota_1 = float(input('Insira a primeira nota '))
peso_1 = int(input('Insira o peso da primeira nota '))
nota_2 = float(input('Insira a segunda nota '))
peso_2 = int(input('Insira o peso da segunda nota '))
nota_3 = float(input('Insira a terceira nota '))
peso_3 = int(input('Insira o peso da terceira nota '))

# Processamento 
media_ponderada = (nota_1 * peso_1 + nota_2 * peso_2 + nota_3 * peso_3) / (peso_1 + peso_2 + peso_3)

# Saída
print(f'A media ponderada das notas do aluno equivale a {media_ponderada}')