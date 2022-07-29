sexo = str(input('Digite seu sexo [M ou F]: ')).strip().upper()[0]

while sexo not in 'MF':
    print('Comando invalido, tente novamente')
    sexo = str(input('Digite seu sexo [M ou F]: ')).strip().upper()[0]
print('Sexo {} regisrado com sucesso'.format(sexo))