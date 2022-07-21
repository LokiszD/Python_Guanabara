din = round(float(input('Saldo na sua carteira: ')), 2)
dolar = round((din/3.27), 2)

print('Voce têm {} R$'.format(str(din).replace('.', ',')))
print('E pode comprar {} US$'.format(str(dolar).replace('.', ',')))