numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

n = int(input('Posição que quer ver: '))
while True:
    if 0 <= n <= 20:
        break
    print('Invalido, digite novamente...')
    n = int(input('Posição que quer ver: '))

print(numeros[n])