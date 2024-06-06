# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

listagem = ("lapis", 1.75,
            "borracha", 2,
            "caderno", 15.90,
            "estojo", 25,
            "transferidor", 4.20,
            "compasso", 9.99,
            "mochila", 120.32,
            "caneta", 22.30,
            "livro", 34.90,)
print("-"*40)
print(f"{'LISTAGEM DE PRECOS':^40}")
print("-"*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f"{listagem[pos]:.<30}", end= "")
    else:
        print(f"R${listagem[pos]:>7.2f}")
print("-"*40)

# ------------------ fim do codigo ------------------#
# if foi feito para pegar as posicoes pares
# else pega as posicoes impares
# posicoes pares alinhado a esquerda e impares na direita