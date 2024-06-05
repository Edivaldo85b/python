# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) 
# e mostrá-lo por extenso.

cont = ("zero" ,"um", "dois", "tres", "quatro",
"cinco","seis", "sete", "oito","nove", "dez",
"onze", "doze", "treze", "quatorze", "quinze"
"dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

while True:
    num = int(input("Digite um numero entre 0 e 20: "))
    if 0 <= num <= 20:
        print(f"Voce digitou o numero {cont[num]}")
        continuar = str(input("Deseja continuar [S / N]")).strip().upper()
        if continuar == "N":
            break
    print("Tente novamente", end=" ")

# -------------------- Fim do codigo -------------------- #
# foi criado a tupla com os numeros por extenso
# no print foi colocado cont para a tupla e dentro do parentes num para mostrar o numeros
#acrescentei a funcao de perguntar se gostaria de continuar que foi lancado como desafio no video