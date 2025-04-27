# 21. Realize arredondamentos de números utilizando a regra usual da matemática: se a parte fracionaria for
# maior do que ou igual a 0,5, o numero é arredondado para o inteiro imediatamente superior, caso
# contrario, é arredondado para o inteiro imediatamente inferior.

from l2_q15_horas_aulas import obter_numero_racional

def main():
    num = obter_numero_racional('Digite um número: ')
    num_arrredondado = arredondar(num)
    print(f'O número "{num}" arredondado é igual a {num_arrredondado}')


def arredondar(num):
    if num % 1 >= 0.5:
        return num - (num % 1) + 1
    elif num % 1 < 0.5 and num % 1 > 0:
        return num - (num % 1) - 1
    elif num % 1 == 0:
        return num
    

main()