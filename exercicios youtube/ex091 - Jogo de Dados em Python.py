# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
# Guarde esses resultados em um dicionário em Python. No final, 
# coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter
jogo = {
    "jogador 1": randint(1,6),
    "jogador 2": randint(1,6),
    "jogador 3": randint(1,6),
    "jogador 4": randint(1,6)
}
ranking = []
print("Valores Sorteados")
for chaves, valores in jogo.items():
    print(f"{chaves} tirou {valores} no dado.")
    sleep(1)
ranking = sorted(jogo.items(), key = itemgetter(1), reverse = True)
print("-="*30)
print("  == Ranking dos Jogadores ==")
for indice , valores in enumerate(ranking):
    print(f"   {indice+1}º lugar: {valores[0]} com {valores[1]}.")
    
# ---------- fim do codigo ---------- #
# foi importado randint para sortear os numeros de 1 a 6
# foi importado sleep para dar um pausa entre um jogar e outro.
# foi importado o itemgetter para colocar em ordem de valor ,mas ficou bem confuso pq não foi explicado direito,quebri
# a cabeça tentando fazer e encontrei varios lugares usando lambda
# foi criado o dicionário jogo e os Jogadores para sortear os numeros
# foi criado ranking primeiro como um dicionario e depois foi mudado para lista
# o for vai percorrer o dicionário mostrando o resuldado de cada Jogador
# ranking vai ordenar o maior resulado por ultimo e o reverse vai colocar o maior por primeiro
# o for vai enumerar na ordem os Jogadores com os resultados.