# 2. Leia um valor em horas e um valor em minutos, calcule e escreva o equivalente em minutos.

#Entrada
horas = int(input('Digite as horas: '))
minutos = int(input('Digite os minutos: '))

#Processamento
conversao_minutos = (horas * 60) + minutos

#Saida
print (f'{horas}h e {minutos}min equivalem a {conversao_minutos} minutos!!')