from random import randint

computador = randint(0, 10)
n = int(input('Adivinhe: '))
cont = 1

while n != computador:
    if n < computador:
        print('Mais... Tente novamente')
    else:
        print('Menos... Tente novamente')
    n = int(input('Adivinhe: '))
    cont += 1
print('Parabens! Voce adivinhou depois de {} tentativas'.format(cont))