from random import randint

num = int(input('Descubra o valor aleatorio de 1 a 5: '))

numAleatorio = randint(1, 5)

if num == numAleatorio:
    print('Parabens! Voce acertou')
else:
    print('Que pena, tente novamente')
print('Numero aleatório: {}, seu numero: {}'.format(numAleatorio, num))
