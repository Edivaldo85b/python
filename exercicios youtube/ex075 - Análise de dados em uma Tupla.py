# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

numero = (int(input("Digite um numero: ")),int(input("Digite outro numero: ")),int(input("Digite mais um numero: ")),int(input("Digite ultimo numero: ")))
print(f"Voce digitou os valores {numero}")
print(f"O valor 9 apareceu {numero.count(9)} vezes")
if 3 in numero:
    print(f"O valor 3 apareceu na {numero.index(3)+1} posicao")
else:
    print("O valor 3 nao foi digitado em nenhuma posição")
print("os valores pares digitados foram ", end = " ")
for par in numero:
    if par % 2 == 0:
        print(par, end = " ")
        
# --------------- fim do codigo ---------------#
# tinha pensado em fazer a pergunta com um for algo do tipo:
# for c in range(1, 5):
#   valores= tuple(int(input('Digite um número:  ')))