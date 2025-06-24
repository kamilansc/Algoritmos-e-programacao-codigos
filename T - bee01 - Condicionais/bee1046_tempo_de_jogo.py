def main():
    entrada = input().split()
    hora_inicio = int(entrada[0])
    hora_fim = int(entrada[1])

    if hora_fim > hora_inicio:
        print(f'O JOGO DUROU {hora_fim-hora_inicio} HORA(S)') 
    elif hora_inicio == hora_fim:
        print(f'O JOGO DUROU 24 HORA(S)')
    elif hora_fim < hora_inicio:
        print(f'O JOGO DUROU {24-hora_inicio + hora_fim} HORA(S)')


main()