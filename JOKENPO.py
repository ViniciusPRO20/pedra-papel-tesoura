from random import randint
from time import sleep

n = 1
while n != 0:
    itens = ('pedra', 'papel', 'tesoura')
    PC = randint(0, 2)
    print('''Suas opcões:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA
    [ 3 ] SAIR''')
    jogador = int(input("Qual você quer jogar? "))
    if jogador == 3:
        print("Você saiu do game")
        break
    print('PEDRA')
    sleep(1)
    print('PAPEL')
    sleep(1)
    print('TESOURA!!!')
    print("><" * 12)
    print("O computador jogou {}".format(itens[PC]))
    print("Você jogou {}".format(itens[jogador]))
    print("><" * 12)
    if PC == 0:
        if jogador == 0:
            print("EMPATE")
        elif jogador == 1:
            print("JOGADOR VENCEU")
        elif jogador == 2:
            print("COMPUTADOR VENCEU")
        else:
            print("Jogada invalida")
    elif PC == 1:
        if jogador == 0:
            print("COMPUTADOR VENCEU")
        elif jogador == 1:
            print("EMPATE")
        elif jogador == 2:
            print("JOGADOR VENCEU")
        else:
            print("Jogada invalida")
    elif PC == 2:
        if jogador == 0:
            print("JOGADOR VENCEU")
        elif jogador == 1:
            print("COMPUTADOR VENCEU")
        elif jogador == 2:
            print("EMPATE")
        else:
            print("Jogada invalida")
        
        

