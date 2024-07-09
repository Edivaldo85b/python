# Cria um programa que gerencia o aprovaitamento de um jogador
# de futebol. O programa vai ler o nome do jogador e quantas
# partidas ele jogou. Depois vai ler a quantidade de gols feitos em
# cada partida. No final, tudo isso sera guardado em um dicionário.
# Incluindo o total de gols feitos durante o campaonato.
#  095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogador = {}
time = []
partidas = []
while True:
    jogador.clear()
    jogador["Nome"] = str(input("Nome do Jogador: "))
    total_partidas = int(input(f"Quantas partidas {jogador['Nome']} jogou ?"))
    partidas.clear()
    for contador in range (0, total_partidas):
        partidas.append(int(input(f"    Quantos gols na partida {contador+1}? ")))
    jogador["Gols"] = partidas[:]
    jogador["Total"] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resposta = str(input("Deseja continuar ? [ S / N]")).upper()[0]
        if resposta in "SN":
            break
        print("ERRO !!! Responda apenas S ou N")
    if resposta == "N":
            break
print("-="*30)
print("cod", end=" ")
for elemento in jogador.keys():
    print(f"{elemento:<15}", end=" ")
print()
print("-"*40)
for chave, valor in enumerate(time):
    print(f"{chave:>3}", end=" ")
    for dados in valor.values():
        print(f"{str(dados):<15}", end=" ")
    print()
print("-"*40)
while True:
    busca = int(input("Mostra dados de qual jogador ? [999] para encerrar "))
    if busca == 999:
        break
    if busca >= len(time):
        print(f"ERRO !!!! Nao existe jogador com o codigo {busca}")
    else:
        print(f" -- LEVANTAMENTO DO JOGADOR {time[busca]['Nome']}")
        for indice, gols in enumerate(time[busca]["Gols"]):
            print(f"    No jogo {indice+1} fez  {gols} Gols.")
    print("-"*40)
print("<< VOLTE SEMPRE >>")
# ---------- fim do codigo ---------- #
# jogador é um dicionário vazio e partidas uma lista vazio
# total_partidas é uma variavel simples
# for vai capturar a quantidade de gols e salvar na lista partidas
# jogador["gols"] = partidas [:] vai fazer uma copia da lista partidas para o dicionário jogador gols
# jogador["Total"] vai somar os gols feitos nas partidas
#print vai mostrar em forma de dicionario
#for vai mostra separado e formatado o dicionario
# o indice e valor vai mostrar formatado os dados do jogado