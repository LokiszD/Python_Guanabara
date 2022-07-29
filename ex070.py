
totalGasto = 0
maisde1000 = 0
cont = 1
while True:
    print(f'Produto {cont}')
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: '))
    print('')

    # total gasto
    totalGasto += preco

    # quantos produtos custam mais de 1000
    if preco > 1000:
        maisde1000 += 1

    # nome do produto mais barato
    if cont == 1:
        maisBarato = nome
        precoBarato = preco
    else:
        if preco < precoBarato:
            maisBarato = nome

    # pergunta ao usuario se quer continuar
    digito = str(input('Quer continuar? [S / N]: ')).strip().upper()
    while digito != 'S' and digito != 'N':
        print('Letra inválida, tente novamente...')
        digito = str(input('Quer continuar? [S / N]: ')).strip().upper()
    if digito == 'N':
        break
    cont += 1
    print('')

print(f'Total gasto na compra: R$ {totalGasto:.2f}')
print(f'Um total de {maisde1000} produtos custam mais de R$1.000,00 reais')
print(f'O produto mais barato é o {maisBarato.upper()}')