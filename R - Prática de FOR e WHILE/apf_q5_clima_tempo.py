from funcoes_uteis import ler_num_int, ler_num_float

def main():
    maior_temperatura = float('-inf')
    menor_umidade = float('inf')
    qtd_vezes_temp_exced = 0

    qtd_horas = ler_num_int('Quantidade de horas monitoradas: ')
    lmt_temperatura = ler_num_float('Limite de temperatura: ')

    for hora in range(1, qtd_horas + 1):
        print(f'\n-- Hora {hora} --')
        temperatura = ler_num_float('Temperatura: ')
        umidade = ler_num_int('Umidade: ')

        if temperatura > maior_temperatura:
            maior_temperatura = temperatura
        
        if umidade < menor_umidade:
            menor_umidade = umidade
        
        if temperatura > lmt_temperatura:
            qtd_vezes_temp_exced += 1

    print(f'\n{3*' '}Maior temperatura: {maior_temperatura}')
    print(f'{3*' '}Menor umidade registrada: {menor_umidade}')
    print(f'{3*' '}Quantidade de vezes que a temperatura execedeu: {qtd_vezes_temp_exced}')


main()