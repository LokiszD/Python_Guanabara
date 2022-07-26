from random import choice

print('-='*20)
print('Jokenpo')
print('-='*20)

n = str(input('Pedra, papel ou tesoura?: ').upper())
jokenpo = ['PEDRA', 'PAPEL', 'TESOURA']

computador = choice(jokenpo)

print('Você escolheu {} e o computador escolheu {}'.format(n, computador))

if (computador == 'PEDRA' and n == 'TESOURA') or (computador == 'TESOURA' and n == 'PAPEL') or (computador == 'PAPEL' and n == 'PEDRA'):
    print('Você Perdeu!')
elif (n == 'PEDRA' and computador == 'TESOURA') or (n == 'TESOURA' and computador == 'PAPEL') or (n == 'PAPEL' and computador == 'PEDRA'):
    print('Voce Ganhou!')
else:
    print('Empate')