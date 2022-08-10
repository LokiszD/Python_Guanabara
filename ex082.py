lista = []
listaPar = []
listaImpar = []
digito = 'S'

while True:
    n = int(input('Numero: '))
    lista.append(n)

    digito = (str(input('Quer continuar? [S/N]: '))).strip().upper()

    if digito not in 'SN':
        print('Inválido, tente novamente...')
        digito = (str(input('Quer continuar? [S/N]: '))).strip().upper()

    if digito == 'N':
        break

for i in range(0, len(lista)):
    if lista[i] % 2 == 0:
        listaPar.append(lista[i])
    else:
        listaImpar.append(lista[i])

print(f'\nLista Principal: {lista}')
print(f'Lista de Pares: {listaPar}')
print(f'Lista de Impares: {listaImpar}')