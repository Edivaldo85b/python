# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep

def maior(* numeros):
    contador = maior = 0
    print("-="*30)
    print("\nAnalizando os valores passados...")
    for valor in numeros:
        print(f"{valor}", end=" ", flush=True)
        sleep(0.3)
        
        if contador == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        contador = contador + 1
    print(f"Foram informado {contador} valores ao todo.")
    print(f"O maior valor informado foi {maior}.")



maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0 )
maior(1, 2)
maior(6)
maior()

# -------------- fim do codigo -------------- #
# foi import sleep da bibliote time para fazer a pausa na contagem
# for vai percorrer os valores dentro do def maior 
# if vai testar se o primeiro numero é igual a zero para definir o maior
# else vai definir o maior numero
#print vai mostrar a quantidade de numero e o maior numero