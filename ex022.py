nome = str(input('Coloque seu nome completo: '))

nomeUpper = nome.upper()
print('Seu nome em maiusculo: {}'.format(nomeUpper))

nomeMin = nome.lower()
print('Seu nome em minusculo: {}'.format(nomeMin))

total = len(''.join(nome.split()))
print('Total de letras no nome: {}'.format(total))

totalPrimeiro = len(nome.split()[0])
print('Quantas letras no primeiro nome: {}'.format(totalPrimeiro))