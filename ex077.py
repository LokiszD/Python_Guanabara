listagem = ('antonio', 'vermelho', 'roxo', 'saudade', 'alegria')

for i in listagem:
    print(f'Na palavra {i} temos ', end=' ')
    for letra in i:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
    print('')
