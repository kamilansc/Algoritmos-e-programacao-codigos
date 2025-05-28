'''Exemplo de Uso (break e continue):
Pedir 6 números ao usuário. Se
digitar 0 para imediatamente. Se
digitar valor negativo não
considerar.'''

from funcoes_uteis import obter_num_int

for i in range (1, 7):
    num = obter_num_int('Número: ')
    if num == 0:
        print('Você digitou 0, então STOP!')
        break
    elif num < 0:
        print('Você digitou um número negativo. DESCONSIDERADO!')
        i -= 1 # ATENÇÃO! esse decremento não funciona utilizando o for dessa forma, pois quem está controlado o 'i'
               # é a função range(), se for realmente necessário controlar o 'i', então é melhor utilizar o while.
               # Porém há um truque com for que é possível fazer esse controle, abaixo um código com exemplo disso:


valores_aceitos = 0 
for i in range(100):  # Um número bem grande para garantir tentativas suficientes
    if valores_aceitos >= 6: # Nesse caso a variável valores_aceitos me permite controlar o decremento de 6 (linha 35)
        break

    numero = int(input(f"Digite o {valores_aceitos + 1}º número: "))

    if numero == 0:
        print("Número 0 digitado. Encerrando.")
        break

    if numero < 0:
        print("Número negativo ignorado.")
        continue

    print(f"Número aceito: {numero}")
    valores_aceitos += 1