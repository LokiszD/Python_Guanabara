cont = 0

for i in range(1, 7):
    num = int(input('n{} :'.format(i)))
    if num % 2 == 0:
        cont += num
        print('par')
    else:
        print('impar')
print('A soma de todos pares é = {}'.format(cont))