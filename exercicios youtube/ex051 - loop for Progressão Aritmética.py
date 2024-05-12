 # Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
 # No final, mostre os 10 primeiros termos dessa progressão.
 
primeiro = int( input("Primeiro termo: "))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for contador in range(primeiro, decimo + razao, razao):
    print(f'{contador}', end= " -> ")
print('Acabou !!!')

# -------------- fim do codigo -------------- #

# dentro do for foi substituido os numero pelas variaveis que foi criada
# a variavel decimo foi criado para descobrir o 10 termo da P.A