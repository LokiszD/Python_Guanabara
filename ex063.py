print('-'*25)
print('Sequencia de Fibonacci')
print('-'*25)

n = int(input('n1: '))
t1 = 0
t2 = 1
cont = 0
print('{} -> {} ->'.format(t1, t2), end=' ')
while cont < n - 2:
    t3 = t1 + t2
    print('{} ->'.format(t3), end=' ')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
