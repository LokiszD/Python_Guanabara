
lista = []

for i in range(0, 5):
    n = int(input(f'Numero {i}: '))
    if i == 0 or  n > lista[-1]:
        lista.append(n)



print(lista)