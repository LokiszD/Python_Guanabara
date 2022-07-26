n1 = float(input('Nota 1:'))
n2 = float(input('Nota 2:'))

media = (n1+n2) / 2
print('Media: {:.2f}'.format(media))

if media < 5:
    print('REPROVADO')
elif 5 <= media < 7:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')