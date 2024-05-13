# Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pessoa in range(1, 8):
    nascimento = int(input(F'Em que ano a {pessoa} pessoa nasceu ? '))
    idade = atual - nascimento
    if idade >= 21:
        totalmaior = totalmaior + 1
    else:
        totalmenor = totalmenor + 1
        
print(f'Ao todo tivemos {totalmaior} pessoas maiores de idade')
print(f'Ao todo tivemos {totalmenor} pessoas menores de idade')