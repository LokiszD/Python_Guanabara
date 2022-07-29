p = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))

i = p
fim = p + 10 * razao
while i < fim:
    print(i, end=' ')
    i += razao

