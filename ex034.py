sal = float(input('Escreva seu salario: '))

if sal > 1250:
    novoSal = sal * 1.1
    print('Aumento de 10%')
else:
    novoSal = sal * 1.15
    print('Aumento de 15%')
print('Seu novo salario é de R$ {:.2f}'.format(novoSal))

