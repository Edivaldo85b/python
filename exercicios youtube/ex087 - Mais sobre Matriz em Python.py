# Exercício Python 087: Aprimore o desafio anterior, mostrando no final: 
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
matriz = [[],[],[]]
soma_par = maior_valor = soma_coluna = 0
for linha in range(0,3):
        for coluna in range(0,3):
                matriz[linha].append(int(input(f"Digite um valor para [{linha},{coluna}]: ")))
print('-='*30)
for linha in range(0,3):
        for coluna in range(0,3):
                print(f'[{matriz[linha][coluna]:^5}]', end='')
                if matriz [linha] [coluna] % 2 == 0:
                    soma_par = soma_par + matriz [linha] [coluna]
        print()
print(f"-=" * 30 , f"\nA soma dos pares é {soma_par}.")
for linha in range(0, 3):
    soma_coluna = soma_coluna + matriz [linha] [2]
print(f"A soma das colunas é {soma_coluna}.")
for coluna in range (0, 3):
    if coluna == 0:
        maior_valor = matriz [1] [coluna]
    elif matriz [1] [coluna] > maior_valor:
        maior_valor = matriz [1] [coluna]
print(f"O maior valor da segunda linha é {maior_valor}.")