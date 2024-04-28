# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
pc = randint(0,5)
print(f"{'-=-'*20} \n Vou pensar em um numero entre 0 e 5 tente adivinha...\n{'-=-'*20}")
user = int(input("Em qual numero o computador pensou de 0 a 5 ? "))
if pc == user :
    print(f"O computador pensou {pc} você venceu !")
else:
    print(f"O computador pensou {pc} você perdeu !")


#---------- fim do codigo ----------#

# randint faz o pc randorizar um numero
# if ,se for igual == ganhou ,else senão perdeu