algo = input('Digite algo: ')

print('Tipo primitivo: {}'.format(type(algo)))
print('É um numero? {}'.format(algo.isnumeric()))
print('É alfabético? {}'.format(algo.isalpha()))
print('É minuscula? {}'.format(algo.islower()))
print('É alfanumerico? {}'.format(algo.isalnum()))