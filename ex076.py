print('-' * 35)
print('Listagem de Preços')
print('-' * 35)

listagem = ('Leite', 7.50, 'Toddy', 5, 'Atum', 3.50, 'Salame', 14.50)

for i in range(0, len(listagem), 2):
    print(f'{listagem[i]:.<25}', end='')
    print(f'R${listagem[i + 1]:>7.2f}')
print('-' * 35)
