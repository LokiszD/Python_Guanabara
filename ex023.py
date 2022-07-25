n = int(input('Insira um Número de 0 a 9999: '))

if n<0 or n>9999:
    print('numero invalido, insira de novo')
    n = int(input('Insira um Número de 0 a 9999: '))

u = n // 1 % 10
d = n // 1 % 100
c = n // 1 % 1000
m = n // 1 % 10000

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))