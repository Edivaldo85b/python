# Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possiveis sobre ela.
algo = input("Digite algo: ") # criado a variavel algo para receber a entrada do teclado
print("O tipo primitivo desse valor é : ", type (algo))# se tivesse apenas essa linha iria sempre retornar que é uma string
print("Só tem espaços ? ", algo.isspace()) # verifica se tem espaços
print("É um numero ? ", algo.isnumeric()) # verifica se é numero
print("É alfabetico ? ", algo.isalpha()) # verifica se é letra
print("É alfanumerico ? ", algo.isalnum()) # verifica se é letra e numero
print("É maiusculo ? ", algo.isupper()) # verifica se é maiusculo
print("É minusculo ? ", algo.islower()) # verifica se é minusculo

# retorna verdadeiro ou falso

#---------- Fim do codigo ----------#