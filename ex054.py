from datetime import date

anoAtual = date.today().year
deMenor = 0
deMaior = 0
for i in range(0, 7):
    ano = int(input('Ano de Nascimento, {}º pessoa: '.format(i+1)))
    idade = anoAtual - ano
    print('Idade: {} anos\n'.format(idade))
    if idade < 21:
        deMenor += 1
    else:
        deMaior += 1
print('Um total de {} pessoas ainda não atingiram a maioridade, e {} pessoas são de maior (maioridade = 21 anos)'.format(deMenor, deMaior))
