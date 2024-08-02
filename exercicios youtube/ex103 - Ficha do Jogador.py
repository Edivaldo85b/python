# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado 

def ficha(jogador="<Desconhecido>", gol=0):
    print(f"O jogador {jogador} fez {gol} gol(s) no jogo.")
    
    
nome = str(input("Nome do Jogador: "))
gols = str(input("Numero de Gols: "))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == "":
    ficha(gol=gols)
else:
    ficha(nome, gols)
    
# ------------------- fim do codigo ------------------- #
#definimos a ficha para comecar com o jogador Desconhecido caso nao seja preenchido e gols com zero
# usa string em gols para poder ficar vazia ja que numero inteiro não pode ficar vazio
#o if vai verificar se foi digitado numero ou letra e se for vazio vai preencher com zero.
# outro if vai testar se o nome ficou vazio e preencher com Desconhecido senao vai usar o nome preenchido