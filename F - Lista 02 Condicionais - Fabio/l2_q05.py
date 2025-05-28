from funcoes_uteis import obter_numero_inteiro

# Leia 3 (três) números e escreva-os em ordem crescente.

def main():
    label = 'Digite um número: '
    a = obter_numero_inteiro(label)
    b = obter_numero_inteiro(label)
    c = obter_numero_inteiro(label)

    if a <= b and b <= c:
        print(f'Ordem crescente: {a} ; {b} ; {c}')
    elif a <= c and c <= b:
        print(f'Ordem crescente: {a} ; {c} ; {b}')
    elif b <= a and a <= c:
        print(f'Ordem crescente: {b} ; {a} ; {c}')
    elif b <= c and c <= a:
        print(f'Ordem crescente: {b} ; {c} ; {a}')
    elif c <= a and a <= b:
        print(f'Ordem crescente: {c} ; {a} ; {b}')
    elif c <= b and b <= a:
        print(f'Ordem crescente: {c} ; {b} ; {a}')


main()