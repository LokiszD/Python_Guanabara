n = str(input('Digite uma expressão com (parenteses): '))

contAbre = 0
contFecha = 0
for letra in n:
    if letra == '(':
        contAbre += 1
    elif letra == ')':
        contFecha += 1

if contAbre == contFecha:
    print('Expressão Válida!')
else:
    print('Expressão não é valida')
