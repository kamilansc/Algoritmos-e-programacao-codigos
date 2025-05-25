entrada = int(input())
n = entrada

def confere_palindromo(n):
    binario = bin(n)[2:]
    return binario == binario[::-1]

while n > 0:
    if confere_palindromo(n):
        print(n)
        break
    n -= 1