n = int(input('Numero: '))

soma = 0  # para fazer a media
cont = 0  # para fazer a media
maior = menor = 0
digito = 'S'

while digito == 'S':
    if cont == 0:
        maior = menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    soma += n
    cont += 1

    digito = str(input('Deseja adicionar mais numeros? [S/N]: ')).strip()[0].upper()
    if digito == 'S':
        n = int(input('Numero: '))

media = soma / cont
print('Media: {}'.format(media))
print('Maior: {}\nMenor: {}'.format(maior, menor))