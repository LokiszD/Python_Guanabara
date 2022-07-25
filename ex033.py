n1 = float(input('n1: '))
n2 = float(input('n2: '))
n3 = float(input('n3: '))

if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:
    menor = n2
else:
    menor = n3
print('Menor Número: {}'.format(menor))

if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
else:
    maior = n3
print('Maior Número: {}'.format(maior))