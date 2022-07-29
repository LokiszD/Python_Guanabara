soma = 0
cont = 0

while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    soma += n
    cont += 1

print(f'A soma desses numero foi: {soma}, em um total de {cont} numeros somados')