# Início: 25/05 19h41
# Fim:    25/05 20h18

from q1_number_utils import obter_num_int
def main():
    qtd_entrevistas = obter_num_int('Quantidade de entrevistas: ')

    backend = 0
    frontend = 0
    dados = 0
    mobile = 0
    total = 0

    while qtd_entrevistas > 0:
        infos = input('Resultado da primeira entrevista: ')
        qtd_pessoas = int(infos.split() [0])
        area = infos.split() [1]

        if area == 'B':
            backend += qtd_pessoas
        elif area == 'F':
            frontend += qtd_pessoas
        elif area == 'M':
            mobile += qtd_pessoas
        elif area == 'D':
            dados += qtd_pessoas
        
        total += qtd_pessoas
        qtd_entrevistas -= 1

    percent_back = calcular_porcentagem(backend, total)
    percent_front = calcular_porcentagem(frontend, total)
    percent_mobi = calcular_porcentagem(mobile, total)
    percent_dados = calcular_porcentagem(dados, total)


    print(f'''
    Total: {total} alunos
    Total de Backend: {backend}
    Total de Frontend: {frontend}
    Total de Mobile: {mobile}
    Total de Dados: {dados}
    Percentual de Backend: {percent_back:.2f}% 
    Percentual de Frontend: {percent_front:.2f}% 
    Percentual de Mobile: {percent_mobi:.2f}% 
    Percentual de Dados: {percent_dados:.2f}% ''')


def calcular_porcentagem(qtd_area, qtd_total_pessoas):
    return (qtd_area/qtd_total_pessoas)*100


main()