diasAlugado = int(input('Quantos dias foi alugado? :'))
km = float(input('Quantos km rodado? :'))

custoCar = diasAlugado * 60
custoKM = km * 0.15
precoTotal = custoCar + custoKM

print('Custo dos dias alugado foi R${} e da KM foi R${}, \nTotal: {:.2f}'.format(custoCar, custoKM, precoTotal))