# 6. Escreva a tabuada dos números de 1 a 10.

def main():
    multiplo = 0
    numero = 1
    efetuar_tabuada(multiplo, numero)
   

def efetuar_tabuada(multiplo, numero):
    while True:
        multiplo += 1
        if numero in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and multiplo == 1:
            print(f'\n   >>> Tabuada do {numero} <<<')
        print(f'\t{numero} x {multiplo} = {numero * multiplo}')
        if multiplo == 10:
            numero += 1
            multiplo = 0
        if numero == 11:
            break

main()