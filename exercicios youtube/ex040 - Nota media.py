#  Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

print(f"{'-=-' *10}\n Calcular nota media \n{'-=-' *10}")
nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunga nota: "))
media = (nota1 + nota2) /2
print(f"Tirando {nota1} e {nota2} a media é {media}")

if media < 5:
    print("O aluno esta Reprovado")
elif media > 5 and media < 7:
    print("O aluno esta em Recuperação")
else:
    print("O aluno esta Aprovado")
    
#---------- fim do codigo ----------#