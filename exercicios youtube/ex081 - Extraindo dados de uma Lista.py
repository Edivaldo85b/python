# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
    lista1 = str(input("Digite um valor: "))
    lista.append(lista1)
    
    resposta = str(input("Deseja continuar ? [ S / N ]")).strip().upper()[0]
    if resposta not in "S":
        break
    
print(f"Voce digitou {lista1} elementos.")
print(f"Os valores em ordem decrescente são {sorted(lista, reverse=True)}.")
if lista == 5 :
    print("O número 5 faz parte da lista.")
else:
    print("Nao encontrei o número 5")
    
# ------------ fim do código ------------ #
# comecamos com um lista vazia e criamos o lista1 para armazenar os valores digitados
# usamos o lista.append para passar esses valores para lista
# criamos um variavel resposta para perguntar se o usuário quer continuar 
# achei melhor colocar o sorted diretamente dentro do print,tinha feito uma variável separado so para ordenar
# no if testamos se tem o numero 5 dentro da lista.
