cid = str(input('Sua Cidade: '))

cid = cid.upper().split()


if 'SANTO' in cid:
    print('Sua cidade tem o nome SANTO no nome')
else:
    print('Sua cidade nao tem SANTO no nome')