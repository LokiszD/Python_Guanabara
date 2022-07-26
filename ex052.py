n1 = int(input('n1: '))
cont = 0

for i in range(1, n1+1):
    if n1 % i == 0:
        print('\033[33m', end=' ')
        cont += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(i), end='')

print('')
if cont == 2:
    print('Primo')
else:
    print('Não é primo')