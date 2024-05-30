# Faça um programa que mostre a tabuada de vários números, um de cada vez, 
# para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.


while True:
    numero = int(input("Quer ver a tabuada de qual valor? "))
    if numero < 0:
        print("Programa de tabuada encerrado. Volte sempre!")
        break
    print("-" * 30)
    for contador in range(1, 11):
        print(f"{numero} x {contador} = {numero*contador}")
    print("-" * 30)
# ---------------- fim do codigo ----------------#
# o if foi criado para se digitar um numero negativo encrrar o Programa
# no for foi criado a tabuada que será mostrado