#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random
computador = random.randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    elif jogador < computador:
        print('Mais... Tente mais uma vez.')
    elif jogador > computador:
        print('Menos... Tente mais uma vez.')
print(f'Acertou com {palpites} tentativas. Parabéns!')

# --------------------------- fim do codigo --------------------------- #

# acertou foi colocado como falso para ficar repetindo a mensagem até acertar
# elif foi criado como dica para saber se é maior ou menor o numero
# palpites foi criado para somar as tentativas