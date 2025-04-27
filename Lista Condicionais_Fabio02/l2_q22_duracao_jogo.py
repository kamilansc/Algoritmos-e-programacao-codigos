# 22. Leia a hora do início de um jogo e a hora de fim do jogo (cada hora é composta por 2 variáveis inteiras:
# hora e minuto). Calcule e escreva a duração do jogo (horas e minutos), sabendo-se que o tempo
# máximo de duração do jogo é de 24 horas e que ele pode iniciar-se em um dia e terminar no dia
# seguinte.

from funcoes_uteis import obter_numero_inteiro

def main():
    hora_inicio = obter_numero_inteiro('Digite a hora de início do jogo: ')
    minuto_inicio = obter_numero_inteiro('Digite os minutos de início do jogo: ')
    hora_fim = obter_numero_inteiro('Digite a hora do fim do jogo: ')
    minuto_fim = obter_numero_inteiro('Digite os minutos do fim do jogo: ')

def calcular_duracao_jogo(h_inicio, min_inicio, h_fim, min_fim):
    # duracao_horas = h_fim - h_inicio
    if min_fim < min_inicio:
        h_fim = h_fim - 1
        