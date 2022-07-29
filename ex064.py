n = int(input('Numero: '))
cont = 0
soma = 0

while n != 999:
    cont += 1
    soma += n
    n = int(input('Numero: '))

print('Soma de todos: {}\nTotal de numeros digitados: {}'.format(soma, cont))