# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

from random import sample
lista = list(range(1,61))
jogos = int(input('Quantos jogos você quer jogar: '))
for j in range(1, jogos + 1):
    bilhete = sample(lista,6)
    print(f'Jogo {j}: {sorted(bilhete)}')
    
# ----------- Fim do codigo ----------- #
# foi usado sample para gerar a lista e randonizar o numero ao mesmo tempo
# variavel jogos para perguntar quantos jogos
# for j para contador 
# 1 para comecar no 1 e ir ate o numero de jogos + 1,assim ignorando o indice 0
# bilhete para armazenar a lista de 6 numeros
# print formatado ja em ordem

# no video foi feito completamente diferente,confesso que fiquei bem confuso
# imaginei que teria uma forma bem mais simples de fazer quando busquei na internet