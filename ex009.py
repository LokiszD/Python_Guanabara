n1 = int(input('Escreva um número para tabuada: '))

for i in range(11):
    print('{} X {} = {}'.format(n1, i, (n1*i)))