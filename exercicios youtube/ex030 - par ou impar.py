# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input("Me diga um numero qualquer :  "))
div = numero % 2

if div == 1:
    print(f"O numero {numero} é ÍMPAR")
else:
    print(f"O numero {numero} é PAR")
    
    
#---------- Fim do codigo ----------#

# a variavel div vai pegar o resto da divisão.
# if se for 1 é impar
# else senão é 0 ai é par