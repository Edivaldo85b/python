# Crie um programa que leia o nome completo de uma pessoa e mostre: 
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = str(input("Digite seu nome Completo: ")).strip()
print(f"""Seu nome em maiúsculas é {nome.upper()}
Seu nome em minúsculas é {nome.lower()}
Seu nome tem ao todo {len(nome) - nome.count(" ")} letras
Seu primeiro nome tem {nome.find(" ")} letras""")

#---------- Fim do codigo ----------#

# foi usado strip para cortar os espaços antes e depois
# upper para maiúsculas
# lower para minúsculas
# len(nome) foi usado para contar o nome
# nome.count parar no primeiro espaços
# nome.find para contar só ate o espaço