def main():
    horarios = list(map(int, input().split()))
    hora_inicial, minuto_inicial, hora_final, minuto_final = horarios

    horario_inicio_segundos = hora_inicial*3600 + minuto_inicial*60
    horario_final_segundos = hora_final*3600 + minuto_final*60

    if horario_inicio_segundos == horario_final_segundos:
        qtd_horas = 24
        qtd_minutos = 0
        print(f'O JOGO DUROU {qtd_horas} HORA(S) E {qtd_minutos} MINUTO(S)')
        return
    elif horario_final_segundos < horario_inicio_segundos:
        duracao = (24*3600 - horario_inicio_segundos) + horario_final_segundos
    else:
        duracao = horario_final_segundos - horario_inicio_segundos

    qtd_horas = duracao//3600
    duracao %= 3600
    qtd_minutos = duracao//60


    print(f'O JOGO DUROU {qtd_horas} HORA(S) E {qtd_minutos} MINUTO(S)')


main()