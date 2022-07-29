p = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))

termo = p
cont = 0
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont < total:
        print(termo, end=' ')
        termo += razao
        cont += 1
    mais = int(input('\nQuanto voce quer a mais: '))
print('FIM')

