# Faça um programa que leia o nome e a media de um aluno, quardando tambem a situacao em um dicionario
# no final mostre o conteudo da estrutura na tela.

aluno = {}
aluno["Nome"] = str(input("Nome: "))
aluno["Media"] = float(input(f"Media de {aluno['Nome']}: "))
if aluno["Media"] > 7:
    aluno["Situacao"] = "Aprovado"
elif 5 <= aluno["Media"] < 7:
    aluno["Situacao"] = "Recuperação"
else:
    aluno["Situacao"] = "Reprovado"
    
print("-=" *30)
for key, value in aluno.items():
    print(f"- {key} é igual {value}")
    
# ------------- Fim do codigo ------------- #
# criamos o dicionario aluno vazio
# usamo dentro das chaves nome,media para criar os dados dentro do dicionario que será digitado pelo usuario
# definimos a Situacao do aluno dentro do if para Aprovado,Reprovado,Recuperação