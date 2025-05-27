from q04_text_utils import obter_texto_min
from q02_int_utils import obter_num_int
import math

def main():
    nome = obter_texto_min('Nome: ', 7)
    
    contador = 0
    somatorio = 0
    while contador < len(nome):
        numero = obter_num_int('Número: ')
        if numero == 1:
            break
        elif numero == 2:
            break
        elif num_eh_primo(numero):
            break
        somatorio += numero
        contador += 1

    if somatorio == 0:
        print(f'''
    Somatório = 0
    Média = 0''')
    else:
        media = somatorio/contador
        print(f'''
        Somatório: {somatorio}
        Média: {media:.2f}''')


def num_eh_primo(num):
    contador = 2
    primo = True # no caso se num = 3, ele não entra no while, poderia colocar um if la em main no lugar disso, mas, não quero S2.
    while contador <= int(math.sqrt(num)):
        if num % contador == 0 and contador != num:
            primo = False
        else:
            primo = True
        contador += 1
    return primo


main()