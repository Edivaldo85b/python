# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input("Primeiro valor: "))
n2 = int(input("segundo valor: "))
n3 = int(input("terceiro valor: "))

# menor = min(n1, n2, n3)
# maior = max(n1, n2, n3)

if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
    
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print(f"O menor numero é: {menor}")
print(f"O maior numero é: {maior}")

#---------- fim do codigo ----------#
# ideia do video era testar a logica no if mas tem um jeito bem mais simples de fazer
#poderia ser criado assim: menor = min(n1, n2, n3) maior = max(n1, n2, n3) que é nativo do python
     