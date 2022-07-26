p = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))

for i in range(0, 10):
    print(razao * i + p, end=' ')

print('\nou')

decimo = p + 10 * razao
for i in range(p, decimo, razao):
    print(i, end=' ')