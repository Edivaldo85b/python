# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
soma = 0
cont = 0
for contador in range(1, 7):
    numero = int(input(f'Digite {contador} valor: '))
    if numero % 2 == 0:
        soma = soma + numero
        cont = cont + 1
print(f'Voce informou {cont} Pares numeros e a soma foi {soma}.')

# ---------------- fim do codigo ---------------- #

# novamente cont para contar numeros e soma para somar numeros
# if foi feito para pegar somente os numeros pares