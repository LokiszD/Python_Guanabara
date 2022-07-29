from time import sleep

n1 = float(input('n1: '))
n2 = float(input('n2: '))
i = 0

while i != 5:
    print('''    [1] Somar
    [2]multipicar
    [3]maior
    [4]novos numeros
    [5]sair do programa''')
    i = int(input('Escolha: '))
    if i == 1:
        soma = n1 + n2
        print('-' * 25)
        print('Soma: {}'.format(soma))
        print('-' * 25)
    elif i == 2:
        mult = n1 * n2
        print('-' * 25)
        print('Multiplicação: {}'.format(mult))
        print('-' * 25)
    elif i == 3:
        maior = n1
        if maior < n2:
            maior = n2
        print('-' * 25)
        print('Maior numero: {}'.format(maior))
        print('-' * 25)
    elif i == 4:
        print('-' * 25)
        n1 = float(input('Trocar o n1: '))
        n2 = float(input('Trocar o n2: '))
        print('-' * 25)
print('Encerrando', end='')
for i in range(0, 3):
    print('.', end='')
    sleep(1)
