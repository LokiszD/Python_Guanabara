print('='*25)
print('Bem vindo ao Banco DEV')
print('='*25)
# 50, 20, 10, 1
sacado = int(input('Valor a ser sacado: '))

notas50 = sacado // 50
aux = sacado % 50
notas20 = aux // 20
aux = aux % 20
notas10 = aux // 10
aux = aux % 10
notas1 = aux // 1



print(f'''Total de {notas50} cédulas de R$50,00
Total de {notas20} cédulas de R$20,00
Total de {notas10} cédulas de R$10,00
Total de {notas1} cédulas de R$1,00
''')