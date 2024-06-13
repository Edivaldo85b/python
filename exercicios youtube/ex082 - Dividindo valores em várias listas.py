# Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
lista = []
impares =  []
pares = []
while True:
    lista.append(int(input("Digite um valor: ")))
    
    resposta = str(input("Deseja continuar? [ S / N ]"))
    if resposta not in "Ss":
        break
    
for c in lista:
    if c % 2 == 0 :
        pares.append(c)
    else:
        impares.append(c)
    
print("-="*30)
print(f"A lista completa é {lista}")
print(f"A lista de pares {pares}")
print(f"A lista de ímpares {impares}")

#---------- fim do código ----------#
# foi usado o lista.append para salvar diretamente a lista enquanto é digitado 
# foi criado mais duas listas,uma para salvar ps números pares e outra para ímpares 
# for foi feito diferente do video mas acredito quebo resultado foi o mesmo 
# no vídeo foi usado for i, v in enumerate(lista):
