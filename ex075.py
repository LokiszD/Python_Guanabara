n1 = int(input('Valor 1: '))
n2 = int(input('Valor 2: '))
n3 = int(input('Valor 3: '))
n4 = int(input('Valor 4: '))

caixa = (n1, n2, n3, n4)

print('')
print(f'Todos os valores: {caixa}')
cont9 = 0
for i in caixa:
    if caixa[i] == 9:
        cont9 += 1
    if caixa[i] == 3:
        pos3 = caixa.index(3)
    else:
        pos3 = 'Não encontrado'
    if caixa[i] % 2 == 0:
        print(f'{caixa[i]} é par')

print(f'O valor 9 apareceu {cont9} vezes')
print(f'Posição do número 3: {pos3}')
