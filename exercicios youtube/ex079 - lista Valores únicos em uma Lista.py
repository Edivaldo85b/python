# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final,
# serão exibidos todos os valores únicos digitados, em ordem crescente. 

numeros = []
while True:
    n = int(input("Digite um valor: "))
    if n not in numeros:
        numeros.append(n)
        print("Valor adicionado com sucesso")
    else:
        print("Valor DUPLICADO , não vou adicionar")
    resposta = str(input("Quer continuar ? [ S / N] ")).strip().upper()[0]
    if resposta in "N":
        break
print(f'{"-="*30}', f'\nVocê digitou os valores {sorted(numeros)}')

# ----------- fim do codigo ----------- #
# comecamos com a lista vazia chamada numeros
# criamos outra lista chamada n dentro do loop infinito
# usamos o if para pega o numero da lista n e adicionar a lista numero
# no else ira testar se o numero esta repetido e nao ira adicionar a lista de numeros
# criamos a variavel resposta para testar se o usuário quer continuar digitando os numeros para a lista
# user o print formatado duas vezes dentro de uma linha , no video foi feito mais linhas
# o comando sorted foi criado em uma linha separada no video,mas achei melhor dentro do print formatado.