 # Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
 # No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
 
soma = cont = 0
while True:
    numero = int(input("Digite um Valor: [999 para parar] "))
    if numero == 999:
        break
    cont = cont + 1
    soma = soma + numero
print(f"A soma dos {cont } valores foi {soma}")

# -------------- Fim do codigo -------------- #

# o comando break dentro do if faz a interrupcao sem soma 999 aos valores
# assim resolvendo as " GAMBIARRAS " feitas nos exercicios anteriores.