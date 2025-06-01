print('\n >>> TABUADA DE MULTIPLICAÇÃO DO 1 AO 10 <<<')

multiplicando = 1
for multiplicando in range(1, 10+1):
    print(f'-- TABUADA DO {multiplicando} --')
    
    for i in range(1, 10+1):
        produto = i * multiplicando
        print(f'{multiplicando} x {i} = {produto}')

    print('')