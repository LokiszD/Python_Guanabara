frase = str(input('Escreva uma frase: '))
tam = len(frase)

print('A letra A aparece {} vezes na frase'.format(frase.lower().count('a')))
print('A primeira posição da letra A é: {}'.format(frase.lower().find('a')+1))
print('A ultima posição da letra A é: {}'.format(frase.lower().rfind('a')+1))