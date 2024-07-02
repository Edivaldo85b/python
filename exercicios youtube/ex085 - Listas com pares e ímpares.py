# 085: Crie um programa onde o usuário possa digitar sete valores numéricos 
# e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.
lista_nuneros = [[],[]]
valor = 0
for c in range(1,8):
    valor = int(input(f"digite o {c}° valor: "))
    if valor % 2 == 0:
        lista_nuneros[0].append(valor)
    
    else:
        lista_nuneros[1].append(valor)
        
print(lista_nuneros)
print(f"Os números pares são {sorted(lista_nuneros[0])}.")
print(f"Os números ímpares são {sorted(lista_nuneros[1])}")
 
 
# --------- fim do código --------- #
# foi criado duas listas vazias dentro do lista_nuneros.
# criamos a variável valor para armazenar os números 
# dentro do for testemos se o número é par no if
# nuneros pares sao adicionado na posição 0 e ímpares na posição 1
# usei o comando sorted dentro do print no video foi criado duas linha de comando separado