vel = float(input('Velocidade do Carro: '))

if vel > 80:
    multa = (vel-80) * 7
    print('Você foi multado! Preço da Multa = R$ {:.2f}'.format(multa))
else:
    print('Está tudo OK, sem Multa')