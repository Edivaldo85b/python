# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(lista)
print(f"O aluno escolhido foi {escolhido}")

#---------- Fim do codigo ----------#

# foi importado choice que significa escolha da biblioteca random
# os alunos digitados iram para ima lista
# o choice ira escolher dessa lista