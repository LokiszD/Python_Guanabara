num = int(input('Digite um numero inteiro: '))

print('Digite 1 para transformalo em Binario\nDigite 2 para transformalo em Octal\nDigite 3 para transformalo em Hexadecimal')
escolha = int(input('Digite:'))

if escolha < 1 or escolha > 3:
    print('Dígito Invalido')

if escolha == 1:
    base = bin(num)
elif escolha == 2:
    base = oct(num)
elif escolha == 3:
    base = hex(num)

print('Numero Convertido: {}'.format(base))