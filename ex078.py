valores = []

menor = 0
maior = 0
posMaior = 0
posMenor = 0

for i in range(0, 5):
    valores.append(int(input(f'Valor {i}: ')))
    if i == 0:
        maior = valores[i]
        menor = valores[i]
    if valores[i] >= maior:
        maior = valores[i]
        if maior == valores[i]:
            posMaior = i
    elif valores[i] <= menor:
        menor = valores[i]
        if menor == valores[i]:
            posMenor = i

print(f'Elementos da lista: {valores}')
print(f'O menor valor é {menor} e esta na posição {posMenor}')
print(f'O maior valor é {maior} e esta na posição {posMaior}')
