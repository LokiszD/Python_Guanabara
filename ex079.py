
lista = []
cont = 0
digito = 'S'

while digito != 'N':
    n = int(input(f'Numero {cont}: '))
    if n not in lista:
        lista.append(n)
        cont += 1
    else:
        print('Valor Duplicado, não vou adicionar...\n')
    digito = str(input('Que continuar? [S/N]: ')).upper().strip()
    if digito not in 'SN':
        print('Invalido, tente novamente')
        digito = str(input('Que continuar? [S/N]: ')).upper().strip()


print(f'Lista: {lista.sort()}')