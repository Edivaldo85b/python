 # Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
 
numero = int(input("Digite um numero: "))
Unidade = numero // 1 % 10
Dezena = numero // 10 % 10
Centena = numero // 100 % 10
Milhar = numero // 1000 % 10

print(f"""Analisando o numero {numero}
Unidade: {Unidade}
Dezena: {Dezena}
Centena: {Centena}
Milhar: {Milhar}""")

#--------- Fim do codigo ---------#

# foi pego o resto da divisão para dividir e pode pegar a Unidade,Dezena,Centena,Milhar