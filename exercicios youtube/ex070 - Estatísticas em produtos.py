# Crie um programa que leia o nome e o preço de vários produtos. 
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

total = totmil = menor = cont = 0
while True:
    produto = str(input("Nome do produto: "))
    preco = float(input("Preço: R$ "))
    cont = cont +1
    total = total + preco
    if preco > 1000:
        totmil = totmil +1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resposta = " "
    while resposta not in "SN":
        resposta = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if resposta == "N":
        break
print("{:-^40}".format('Fim do programa'))
print(f"O total da compra foi R$: {total:.2f}")
print(f"Temos {totmil} custando mais de mil reais.")
print(f"O produto mais barato foi {barato} que custa R${menor:.2f}")

#----------------- fim do codigo -----------------#
# primerio if para testar preco acima de mil
# segundo if para testa ,menor preco e dar nome do produto