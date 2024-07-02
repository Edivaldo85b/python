# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

temporario = []
principal = []
maior = menor = 0
while True:
    temporario.append(str(input("Nome: ")))
    temporario.append(float(input("Peso: ")))
    if len(principal) == 0:
        maior = menor = temporario[1]
    else:
        if temporario[1] > maior:
            maior = temporario[1]
        if temporario[1] < menor:
            menor = temporario[1]
    principal.append(temporario[:])
    temporario.clear()
    resposta = str(input("Deseja continuar? [S / N] "))
    if resposta in "Nn":
        break
print("-="*30)
print(f"Ao todo, voce cadastrou {len(principal)} pessoas.")
print(f"O maior peso foi {maior} KG, peso de", end = " ")
for nome in principal:
    if nome[1] == maior:
        print(f"[{nome[0]}]", end = " ")
print(f"\nO menor peso foi {menor} KG peso de", end = " ")
for nome in principal:
    if nome[1] == menor:
        print(f"[{nome[0]}]", end = " ")

# -------------- Fim do codigo -------------- #
# foi criado uma lista temporaria e uma lista principal
# testamos o maior e o menor peso
# passamos a lista temporaria para a principal e limpamos a temporaria
# criamos um for para percorrer a lsita principal marcamos o indice [0] para nomes e o indice [1] para peso
# testamos o maior e menor peso.
