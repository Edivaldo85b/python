# Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

resposta = "S"
soma = quantidade = media = maior = menor = 0
while resposta in "Ss":
    numero = int(input("Digite um numero: "))
    soma = soma + numero
    quantidade = quantidade + 1
    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior :
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input("Deseja continuar ? ").strip()[0].upper())
media = soma / quantidade
print(f"Voce digitou {quantidade} numeros e a media foi {media}")
print(f"O maior valor foi {maior} e o menor valor foi {menor}. ")
print("FIM")

# -------------- Fim do codigo -------------- #
# o primeiro if foi criado para definir o  primeiro numeros como maior e menor numeros
# dentro do else foi foi criado outros if para testar o maior e menor numeros
# 