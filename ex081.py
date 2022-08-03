lista = []
digito = 'S'
cont = 0
tem5 = False
while digito != 'N':
    n = int(input('Numero: '))
    lista.append(n)
    cont += 1
    if n == 5:
        tem5 = True

    digito = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    if digito not in 'SN':
        print('Invalido, digite novamente...')
        digito = str(input('Deseja continuar? [S/N]: ')).upper().strip()

print(f'\nLista de forma descrescente: {sorted(lista, reverse=True)}')
print(f'Foram digitados {cont} valores')
if tem5:
    print('O numero 5 esta na lista')
else:
    print('O numero 5 não esta na lista')