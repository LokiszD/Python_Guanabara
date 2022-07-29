from random import randint

print('-=' * 10)
print('Jogo: Par ou Impar')
print('-=' * 10)

cont = 0
while True:
    # usuario coloca se quer par ou impar e repete caso ele colocar errado
    jog = str(input('PAR ou IMPAR? : ')).strip().upper()
    while jog != 'PAR' and jog != 'IMPAR':
        print('Invalido, escreva PAR ou IMPAR')
        jog = str(input('PAR ou IMPAR? : ')).strip().upper()
    # robo escolhe diferente do que usuario colocou
    if jog == 'PAR':
        robo = 'IMPAR'
    elif jog == 'IMPAR':
        robo = 'PAR'
    print(f'O robo escolheu: {robo}')

    # usuario escolhe o numero para jogar e o robo sorteia
    jogN = int(input('Escolha um Numero: '))
    roboN = randint(0, 10)
    print(f'Numero do robo: {roboN}')
    print('..' * 20)

    resulN = jogN + roboN
    print(f'Resultado: {resulN}')

    # ver se resultado deu par ou impar
    if resulN % 2 == 0:
        resul = 'PAR'
    else:
        resul = 'IMPAR'
    print(f'e deu {resul}')

    # resultado do game
    if resul == jog:
        print('Parabens! Voce ganhou\n')
        cont += 1
    else:
        print('Que pena, a máquina te derrotou')
        break
if cont > 0:
    print(f'Você teve {cont} Vitórias consecultiva(s)')

print('FIM')
