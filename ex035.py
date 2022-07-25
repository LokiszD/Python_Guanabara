print('-='*20)
print('Analizador de Triangulo')
print('-='*20)

r1 = float(input('Primeira Reta: '))
r2 = float(input('Segunda Reta: '))
r3 = float(input('Terceira Reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmento acima podem formar um triangulo')
else:
    print('Impossivel formar um triangulo')