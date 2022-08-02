from random import randint

r1 = randint(0, 50)
r2 = randint(0, 50)
r3 = randint(0, 50)
r4 = randint(0, 50)
r5 = randint(0, 50)

tupla = (r1, r2, r3, r4, r5)

print(f'Tupla com os numeros gerados: {tupla}')
print(f'o Maior valor é {max(tupla)} e o menor é {min(tupla)}')