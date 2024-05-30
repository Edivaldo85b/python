#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos
#de uma Sequência de Fibonacci. 

#Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8
print(f"{'-='*15}\n{'Sequencia de Fibonacci'}\n{'-='*15}" )
numero = int(input("Quantos termos voce quer mostrar? "))
termo1 = 0
termo2 = 1
print(f"{'~'*30}\n{termo1} -> {termo2}", end="")
cont = 3
while cont <= numero:
    termo3 = termo1 + termo2
    print(f" -> {termo3}", end = "")
    termo1 = termo2
    termo2 = termo3
    cont = cont + 1
print(" -> FIM")

# -------------- fim do codigo -------------- #
# variavel termo 1 e 2 inicio com 0 e 1 
# dentro do while foi criado a variavel termo3 para fazer a troca entre a 1 e 2 
# assim nao iria repetir os numeros.