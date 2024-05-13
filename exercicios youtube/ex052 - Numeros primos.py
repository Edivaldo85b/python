# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

total = 0
numero = int(input('Digite um número: '))
for contador in range(1, numero +1):
    if numero % contador == 0:
        print('\033[33m', end=' ')
        total = total + 1
    else:
        print('\033[31m', end=' ')
    print(f'{contador}', end=' ')
print(f'\n\033[mO numero {numero} foi divisivel {total} vezes.')
if total == 2:
    print('E por isso É PRIMO')
else:
    print('E por issi NÃO É PRIMO')
    
# ---------------- fim do codigo ---------------- #

# foi usado as cores para melhor visualização de qual é primo e qual não é;
# amarelo marca os numeros que foi divisivel e vermelho pelos quais não foi
