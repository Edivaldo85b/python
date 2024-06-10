# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []
for c in range(0,5):
    n = int(input("Digite um valor: "))
    if c == 0:
        lista.append(n)
    elif n > lista[-1]:
        lista.append(n)
        print("Adicionado ao final da lista")
    else:
        posicao = 0
        while posicao < len(lista):
            if n <= lista[posicao]:
                lista.insert(posicao, n)
                print(f"Adicionado na posicao {posicao} da lista")
                break
            posicao = posicao + 1
print(f"{'-=' *30}", f"\nOs valores digitados em ordem foram {lista}")

# ----------- Fim do codigo ----------- #
# foi interesante a logica usada para criar a lista sem usar o sorted
# if vai testar o primeiro item da lista
# elif vai testar o ultimo item da lista
# else vai testar em qual posicaoda lista vai ser incluido