dist = float(input('Distancia da Viagem em KM: '))

if dist <= 200:
    pas = dist * 0.5
else:
    pas = dist * 0.45
print('Valor da Passagem: R$ {:.2f}'.format(pas))