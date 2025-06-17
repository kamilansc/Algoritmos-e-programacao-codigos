def main():
    qtd_sessoes = obter_numero_int('Quantidade de sessões do exercício: ')

    sessao_maior_volume = 0
    maior_volume = 0
    volume_sessoes = ''
    qtd_sessoes_metade1 = 0
    qtd_sessoes_metade2 = 0
    somatorio_volume_metade1 = 0
    somatorio_volume_metade2 = 0
    for sessao in range (1, qtd_sessoes+1):
        qtd_repeticoes = obter_numero_int('Número de repetições realizadas: ')
        peso_levantado = obter_numero_int('Peso levantado: ')
        volume_total_sessao = qtd_repeticoes*peso_levantado
        volume_sessoes += f'\n\tVolume total da sessão {sessao}: {volume_total_sessao}'

        if sessao <= qtd_sessoes//2:
            qtd_sessoes_metade1 += 1
            somatorio_volume_metade1 += volume_total_sessao
        else:
            qtd_sessoes_metade2 += 1
            somatorio_volume_metade2 += volume_total_sessao
            
        if volume_total_sessao > maior_volume:
            sessao_maior_volume = sessao
            maior_volume = volume_total_sessao

    media_volumes_metade1 = somatorio_volume_metade1/qtd_sessoes_metade1
    media_volumes_metade2 = somatorio_volume_metade2/qtd_sessoes_metade2

    if media_volumes_metade2 > media_volumes_metade1:
        tendencia_melhora_mensagem = 'Tendência de melhora observada!'
    else:
        tendencia_melhora_mensagem = 'Não houve melhora significativa!'

    print(f'''
    Volume das sessões: {volume_sessoes}
    Sessão com maior volume: {sessao_maior_volume} (volume: {maior_volume})
    Mensagem sobre tendência de melhora: {tendencia_melhora_mensagem}''')


def obter_numero_int(label):
    while True:
        entrada = input(label)

        try:
            return int(entrada)
        except:
            print('O que você digitou não é válido como número inteiro. Tente novamente!')


main()