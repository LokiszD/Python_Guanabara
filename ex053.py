f = str(input('Escreva uma frase: ')).strip().upper()
palavras = f.split()
junto = ''.join(palavras)
inverso = ''

for i in range(len(junto)-1, -1, -1):
    inverso += junto[i]

print('Frase:\n{}\nFrase inversa:\n{}'.format(junto, inverso))
if junto == inverso:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')

