# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
#A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função
# vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep

def sortear(lista):
    print("Sorteando 5 valores da lista: ", end=" ")
    for contador in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f"{n}", end=" ", flush=True)
        sleep(0.3)
    print("PRONTO !!! ")
    
def soma_par(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma = soma + valor
    print(f"Somando os valores pares da {lista}, temos {soma}")

numeros = []
sortear(numeros)
soma_par(numeros)

# ------------------- fim do codigo ------------------- #
# importamos randint para sortear os numeros e sleep para dar uma pequena pausa entre os numeros
# definimos sortear colocando um for para sortear 5 numeros e armazenamos na variavel n com lista.append
# print mostra os numeros sorteados e sleep faz uma pequena pausa entre eles
# definimos soma_par para iniciar com o valor 0 e criamos um for para percorrer os numeros salvos na lista
# no if destamos se o numero é par dividindo por 2 se o resultado for zer é par e armazenamos na variavel soma
# no print mostramos os valores pares da lista.
