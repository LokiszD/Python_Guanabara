vCasa = float(input('Valor da Casa: '))
sal = float(input('Salario do Comprado: '))
anos = int(input('Em quantos ano irá pagar a casa: '))

mes = anos * 12

parcela = vCasa / mes

if parcela <= (sal * 0.3):
    print('Empréstimo feito com sucesso! \nO Valor da parcela será de R$ {:.2f} ao longo de {} Meses'.format(parcela, mes))
else:
    print('Empréstimo Recusado! o Valor da parcela excede 30% do salario')