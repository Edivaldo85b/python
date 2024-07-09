# Cria um programa que gerencia o aprovaitamento de um jogador
# de futebol. O programa vai ler o nome do jogador e quantas
# partidas ele jogou. Depois vai ler a quantidade de gols feitos em
# cada partida. No final, tudo isso sera guardado em um dicionário.
# Incluindo o total de gols feitos durante o campaonato.

jogador = {}
partidas = []
jogador["Nome"] = str(input("Nome do Jogador: "))
total_partidas = int(input(f"Quantas partidas {jogador['Nome']} jogou ?"))
for contador in range (0, total_partidas):
    partidas.append(int(input(f"    Quantos gols na partida {contador+1}? ")))
jogador["Gols"] = partidas[:]
jogador["Total"] = sum(partidas)
print("-="*30, f"\n{jogador}\n", "-="*30)
for chave, valor in jogador.items():
    print(f"O campo {chave} tem valor {valor}")
print("-="*30)
print(f"O Jogador {jogador['Nome']} jogou {total_partidas} partidas.")
for indice, valor in jogador.items():
    print(f"    => Na partida {indice}, fez {valor} gols.")
print(f"Foi um total de {jogador['Total']} gols")

# ---------- fim do codigo ---------- #
# jogador é um dicionário vazio e partidas uma lista vazio
# total_partidas é uma variavel simples
# for vai capturar a quantidade de gols e salvar na lista partidas
# jogador["gols"] = partidas [:] vai fazer uma copia da lista partidas para o dicionário jogador gols
# jogador["Total"] vai somar os gols feitos nas partidas
#print vai mostrar em forma de dicionario
#for vai mostra separado e formatado o dicionario
# o indice e valor vai mostrar formatado os dados do jogado