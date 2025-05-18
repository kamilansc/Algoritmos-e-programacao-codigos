from funcoes_uteis import receber_resposta

# Leia 3 (três) números e escreva-os em ordem crescente.

def main():
    label = 'Digite um número: '
    numero1 = receber_resposta(label)
    numero2 = receber_resposta(label)
    numero3 = receber_resposta(label)

    if numero1<numero2 and numero1<numero3 and numero2<numero3:
        print(f'Ordem crescente: l{numero1} ; {numero2} ; {numero3}')
    elif numero1<numero3 and numero1<numero2 and numero2<numero3:
        print(f'Ordem crescente: b{numero1} ; {numero3} ; {numero2}')
    elif numero2<numero1<numero3:
        print(f'Ordem crescente: k{numero2} ; {numero1} ; {numero3}')
    elif numero2<numero3<numero1:
        print(f'Ordem crescente: c{numero2} ; {numero3} ; {numero1}')
    elif numero3<numero1<numero2:
        print(f'Ordem crescente: d{numero3} ; {numero1} ; {numero2}')
    elif numero3<numero2<numero1:
        print(f'Ordem crescente: e{numero3} ; {numero2} ; {numero1}')




main()