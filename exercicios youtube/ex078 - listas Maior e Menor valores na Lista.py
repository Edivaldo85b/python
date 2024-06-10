# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
# mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 
maior = menor = 0

listanumeros = []
for c in range(0,5):
    listanumeros.append(int(input(f"Digite um valor para a posição {c}: ")))
    if c == 0:
        maior = menor = listanumeros[c]
    else:
        if listanumeros[c] > maior:
            maior = listanumeros[c]
        if listanumeros[c] < menor:
            menor = listanumeros[c]
print("-="*30)
print(f"Voce digitou os valores {listanumeros}")
print(f"O maior valor digitado foi {maior} nas posições ", end ="")
for i, v in enumerate(listanumeros):
    if v == maior:
        print(f"{i}...", end = "")
print(f"\nO menor valor digitado foi {menor} nas posições ", end ="")
for i, v in enumerate(listanumeros):
    if v == menor:
        print(f"{i}...", end = "")
# ----------- fim do codiigo ----------- #
# foi criado o for para repetivar varias vezes
# a funcao append foi adicionado a lista capturar os numeros digitados pelo usuario
# primeiro if para definir o primeiro numero como maior e menor ao mesmo tempo
# os ifs dentro do else para definir qual o maior e o menor numero
# outro for criado para pegar o indice ( i ) e o valor ( v ) como ajuda do enumerate
# foi feito o print do indice com end vazio para continuar na mesma linha