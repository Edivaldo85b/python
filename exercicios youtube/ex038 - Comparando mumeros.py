# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

numero1 = int(input("Primeiro numero: "))
numero2 = int(input("Segundo numero: "))

if numero1 > numero2:
    print("O Primeiro numero é maior que o Segundo numero")
elif numero2 == numero1:
    print("Os numeros são iguais")
else:
    print("O Segundo numero é maior que o Primeiro numero")
    
#----------- fim do codigo -----------#

# if compara se é maior que outro
#elif compara se são iguais
# else compara se é menor

#no video foi feito diferente
#no elif fico numero2 maior que numero1
# else fico p testar se são iguais
    