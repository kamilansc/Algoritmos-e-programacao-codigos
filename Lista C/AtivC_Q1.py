#Leia uma velocidade em m/s, calcule e escreva esta velocidade em km/h. (Vkm/h = Vm/s * 3.6)

velocidade_metros = float(input("Digite a velocidade em m/s: "))

def principal():
    velocidade_quilometros = conversao(velocidade_metros)
    print(f"A velocidade {velocidade_metros}m/s equivale a {velocidade_quilometros}km/h. ")
    
    
# Processamento
def conversao (velocidade_metros):
    velocidade_quilometros = velocidade_metros * 3.6
    return velocidade_quilometros
    
principal()