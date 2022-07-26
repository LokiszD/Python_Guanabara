from datetime import date

anoNasc = int(input('Ano de nascimento: '))

dataAtual = date.today()
anoAtual = dataAtual.year

idade = anoAtual - anoNasc

if idade < 18:
    print('Você ainda irá se alistar, ainda falta {} anos para seu alistamento'.format(18 - idade))
elif idade > 18:
    print('Ja passou da hora de se alistar, esta atrasado em {} anos'.format(idade - 18))
else:
    print('Está na hora de se alistar! É esse ano')