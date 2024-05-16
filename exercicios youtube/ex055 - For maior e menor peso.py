# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for pessoa in range(1, 6):
    peso = float(input(f'Peso da {pessoa}ª pessoa: '))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior} KG')
print(f'O menor peso lido foi de {menor} KG')


# ------------------ fim do codigo ------------------ #

# o primeiro if foi criado para definir o maior e menor peso a primeira pessoa
# o if que esta dentro do else irá fazer o comparativo de peso para o resultado