# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

n = str(input('Digite uma expressão com (parenteses): '))

contAbre = 0
contFecha = 0
valido = True
for letra in n:
    if letra == '(':
        contAbre += 1
    elif letra == ')':
        contFecha += 1

posAbre = n.index('(')
posFecha = n.index(')')

if posAbre > posFecha:
    valido = False

if contAbre == contFecha and valido:
    print('Expressão Válida!')
else:
    print('Expressão não é valida')
