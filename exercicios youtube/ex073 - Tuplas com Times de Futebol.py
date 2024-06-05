# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética. 
# d) Em que posição está o time do Corinthians.

times = ("Vitória", "Juventude", "Criciúma", "Atlético-GO", "Palmeiras",
"Corinthians","São Paulo","Red Bull Bragantino","Flamengo", "Fluminense",
"Vasco da Gama", "Botafogo", "Cruzeiro", "Atlético-MG", "Grêmio", "Internacional",
"Athletico-PR", "Cuiabá", "Bahia", "Fortaleza")

print("-="*15)
print(f"Lista de times do Brasileirao: {times}")
print("-="*15)
print(f"Os cinco primeiros sao: {times[0:5]}")
print("-="*15)
print(f"Os 4 ultimos sao: {times[-4:]}")
print("-="*15)
print(f"Times em ordem alfabetica {sorted(times)}")
print("-="*15)
print(f"Oc Corinthians esta na {times.index('Corinthians')+1} posição")

# ------------- Fim do codigo ------------- #
# para mostrar os cinco primeiros foi de 0 a 5 
#os 4 ultimos foi do menos 4 ate vazio para ir ate o ultimo
#a posicao do Corinthians foi colocado +1 pq foi iginorado a posicao zero.