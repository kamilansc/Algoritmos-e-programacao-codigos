def main():
    entrada1 = input().split()
    dia_inicio = int(entrada1[1])

    horario_inicio = list(map(int, input().split(':')))
    hora_inicio, minuto_inicio, segundo_inicio = horario_inicio

    entrada2 = input().split()
    dia_fim = int(entrada2[1])

    horario_termino = list(map(int, input().split(':')))
    hora_termino, minuto_termino, segundo_termino = horario_termino

    horario_inicio_segundos = dia_inicio*86400 + hora_inicio*3600 + minuto_inicio*60 + segundo_inicio
    horario_termino_segundos = dia_fim*86400 + hora_termino*3600 + minuto_termino*60 + segundo_termino

    duracao_segundos = horario_termino_segundos - horario_inicio_segundos

    qtd_dias = duracao_segundos//86400
    duracao_segundos %= 86400
    qtd_horas = duracao_segundos//3600
    duracao_segundos %= 3600
    qtd_minutos = duracao_segundos//60
    qtd_segundos = duracao_segundos % 60
    
    print(f'{qtd_dias} dia(s)')
    print(f'{qtd_horas} hora(s)')
    print(f'{qtd_minutos} minuto(s)')
    print(f'{qtd_segundos} segundo(s)')


main()