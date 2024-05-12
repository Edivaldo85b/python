# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas Opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO !!!')
sleep(1)
print(f"{'-=-'*8} \nO Computador jogou {itens[computador]} ")
print(f"O Jogador jogou {itens[jogador]}\n{'-=-'*8}")

if computador == 0: # Pedra
    if jogador == 0:
        print('Empatou')
    elif jogador == 1: # Papel
        print('jogador VENCEU')
    elif jogador == 2: # Tesoura
        print('computador VENCEU')
    else:
        print('Jogada INVALIDA')
        
elif computador == 1: # Papel
    if jogador == 0: # Pedra
        print('Computador VENCEU')
    elif jogador == 1: # Papel
        print('Empatou')
    elif jogador == 2: #Tesoura
        print('jogador VENCEU')
    else:
        print('Jogada INVALIDA')
        
elif computador == 2: # Tesoura
    if jogador == 0: # Pedra
        print('Jogador VENCEU')
    elif jogador == 1: # Papel
        print('Computador VENCEU')
    elif jogador == 2: # Tesoura
        print('Empatou')
    else:
        print('Jogada INVALIDA')
        
#-------------- Fim do Codigo --------------#
# Achei o codigo bem logo ,mas como a ideia era de fazer um if dentro do outro foi legal para testar