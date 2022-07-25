nome = str(input('Nome completo: '))

nomeArray = nome.split()
primeiroNome = nomeArray[0]
ultimoNome = nomeArray.pop()

print('Primeiro nome: {}'.format(primeiroNome))
print('Ultimo nome: {}'.format(ultimoNome))