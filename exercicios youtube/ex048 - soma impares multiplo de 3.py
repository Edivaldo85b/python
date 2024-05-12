# Faça um programa que calcule a soma entre todos os números que são múltiplos de três
# e que se encontram no intervalo de 1 até 500.

soma = 0
contador = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        contador = contador + 1
        soma = soma + c
        
print(f"A soma de todos os {contador} valores solicitados é {soma}")

# ------------- fim do codigo ------------- #

# foi aumentado para 501 e adicionado o 2 para ira até  500 somente nos numeros impares
# fooi criado a soma para somar todos os numeros divisiveis por 3 e contador para somar todas a vezes que encontrar
# um numero divisivel por 3