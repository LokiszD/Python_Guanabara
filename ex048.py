soma = 0
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        print(i, end=' ')
        soma += i
        cont += 1

print('\nSoma de todos os números: {}\nTotal de numeros: {}'.format(soma, cont))
