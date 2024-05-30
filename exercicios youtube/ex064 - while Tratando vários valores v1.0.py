# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

contador = soma = numero = 0 # foi juntado todos,pq todos eles recebem o mesmo valor.
numero = int(input("Digite um mumero: [999 para parar] "))# foi colocado esse comando duas vezes para qndo digitar 999 ser iginorado na contagem
while numero != 999:
    contador = contador + 1
    soma = soma + numero
    numero = int(input("Digite um mumero: [999 para parar] "))# foi colocado abaixo do contado e da soma para nao fazer a conta errado
print(f"Voce digitou {contador} e a soma entre eles foi {soma}")
print("FIM")

# ----------------------- fim do codigo ----------------------- #
# Foi explicado essas duas formar de fazer o codigo
# contador = soma = numero = 0
# while numero != 999:
#    numero = int(input("Digite um mumero: [999 para parar] "))
#    contador = contador + 1
#    soma = soma + numero
# print(f"Voce digitou {contador -1 } e a soma entre eles foi {soma - 999}")
# print("FIM")