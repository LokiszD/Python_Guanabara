
maisde18 = 0
contMan = 0
mulherMenosde20 = 0
cont = 1
while True:
    print(f'Pessoa {cont}')
    id = int(input('Idade: '))
    sexo = str(input('[M ou F]: ')).strip().upper()
    cont += 1
    while sexo != 'M' and sexo != 'F':
        print('Sexo invalido, tente novamente...')
        sexo = str(input('[M ou F]: ')).strip().upper()

    print('')
    digito = str(input('Quer continuar? [S / N]: ')).strip().upper()
    while digito != 'S' and digito != 'N':
        print('Letra inválida, tente novamente...')
        digito = str(input('Quer continuar? [S / N]: ')).strip().upper()

    # pessoas com mais de 18 anos
    if id > 18:
        maisde18 += 1
    # quantos homens foram cadastrados
    if sexo == 'M':
        contMan +=1
    # mulheres com menos de 20 anos
    if sexo == 'F' and id < 20:
        mulherMenosde20 += 1

    if digito == 'N':
        break
    print('')

print(f'Um total de {maisde18} pessoas tem mais de 18 anos')
print(f'Foram cadastrados um total de {contMan} homens')
print(f'{mulherMenosde20} mulheres tem menos de 20 anos')