import math

op = float(input('Cateto Oposto do triangulo: '))
ad = float(input('Cateto Adjacente do triangulo: '))

hip = math.hypot(op, ad)

print('Comprimento da Hipotenusa: {:.2f}'.format(hip))