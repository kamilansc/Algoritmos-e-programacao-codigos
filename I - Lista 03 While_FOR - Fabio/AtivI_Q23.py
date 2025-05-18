'''
Uma determinada empresa armazena para cada funcionário uma ficha contendo o código, o número de
horas trabalhadas e o seu no de dependentes. Considerando que a empresa paga R$ 12,00 por hora e R$
40,00 por dependentes e que sobre o salário são feitos descontos de 8,5% para o INSS e 5% para IR.

Escreva um algoritmo que leia o código, número de horas trabalhadas e número de dependentes de N
funcionários. 
Após a leitura de cada ficha, 
escreva os valores descontados para cada imposto e 
o salário líquido do funcionário.'''

from funcoes_uteis import ler_num_int_min, ler_num_racional_min

def main():
    print('\n--> CADASTRO DE FICHA DO FUNCIONÁRIO <--')
    num_funcionarios = ler_num_int_min('Digite o numero de funcionários: ', 0)
    cadastro_ficha_funcionario(num_funcionarios)


def cadastro_ficha_funcionario(num_funcionarios):
    contador = 0
    while contador < num_funcionarios:
        codigo_func = ler_num_int_min('Digite o código do funcionário: ', 0)
        n_horas_trab = ler_num_racional_min('Digite o número de horas trabalhas: ', 0)
        n_dependentes = ler_num_int_min('Digite o número de dependentes: ', 0)
        contador += 1
        print(40*'-')
        print('')
        print(f'Código do funcionário: {codigo_func} -- N° horas trabalhadas: {n_horas_trab} -- N° dependentes: {n_dependentes}')
        calc_salario_liq(n_horas_trab, n_dependentes)


def calc_salario_liq(num_h_trab, n_dependentes):
    salario_bruto = num_h_trab*12 + n_dependentes*40
    desconto_INSS = (8.5/100)*salario_bruto
    desconto_IR = (5/100)*salario_bruto
    salario_liquido = salario_bruto - desconto_INSS - desconto_IR
    print(f'''
    Salário bruto: R$ {salario_bruto:.2f}
    Desconto INSS: R$ {desconto_INSS:.2f}
    Desconto IR:   R$ {desconto_IR:.2f}
    --> Salário líquido: {salario_liquido:.2f}\n''')


main()