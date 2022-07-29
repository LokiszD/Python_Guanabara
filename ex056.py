soma = 0
cont20 = 0
idadeVelho = 0

for i in range(0, 4):
    nome = str(input('Nome - p{}: '.format(i+1)))
    idade = int(input('Idade - p{}: '.format(i+1)))
    sexo = str(input('Sexo (M ou F) - p{}: '.format(i+1)))
    print('')

    soma += idade

    if idade < 20 and sexo == 'F':
        cont20 += 1

    if i == 1 and sexo == 'M':
        maisVelho = nome
        idadeVelho = idade
    elif idade > idadeVelho and sexo == 'M':
        maisVelho = nome
        idadeVelho = idade

media = soma / 4

print('Média de idade do grupo: {} anos'.format(media))
print('Nome do homem mais velho é {} e ele tem {} anos'.format(maisVelho, idadeVelho))
print('Temos {} mulheres com menos de 20 anos'.format(cont20))
