# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
# Ex: Digite um número: 6.127
# O número 6.127 tem a parte Inteira 6.

from math import trunc # foi importado apenas a função trunc da bibliote math
# import math # por primeiro foi importado a biblioteca math Inteira
numero = float(input("digite um valor: "))
# print(f"O valor digitado foi {numero} e sua porção Inteira é {math.trunc(numero)}.") # como a biblioteca toda foi importada 
# foi usado o math antes do trunc.
print(f"O valor digitado foi {numero} e sua porção inteira é {trunc(numero)}") # como foi importado apenas o trunc ,a biblioteca
# nao precisou ser declarada

#---------- Fim do codigo ----------#