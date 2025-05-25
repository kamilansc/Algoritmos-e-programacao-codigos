n = int(input())

s = input()
t = input()

superposicao_s = 0
for i in s:
    if i == '*':
        superposicao_s += 1

superposicao_t = 0
for i in t:
    if i == '*':
        superposicao_t += 1

qtd_num_t = n - superposicao_t
qtd_num_s = n - superposicao_s

colapsaram = qtd_num_t - qtd_num_s

razao = colapsaram/superposicao_s
print(f'{razao:.2f}')