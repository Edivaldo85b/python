# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
# de cada aluno individualmente.

ficha = []
while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota1: "))
    nota2 = float(input("Nota2: "))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resposta = str(input("Deseja continuar ? [ S / N ]"))
    if resposta in "Nn":
        break
print(f"{'-='*30}\n{'N':<4}{'Nome':<10}{'Media':>8}\n{'-'*26}")
for indice, aluno in enumerate(ficha):
    print(f"{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}")
while True:
    print("-"*35)
    opcao = int(input("Mostra nota de qual aluno? (999 FINALIZAR) "))
    if opcao == 999:
        print("...FIM...")
        break
    if opcao <= len(ficha) - 1:
        print(f"Notas de {ficha[opcao][0]} sao {ficha[opcao][1]}")

# ------------- fim do codigo ------------- #
# o primeiro while vai receber as informacoes,nome e Notas
# ficha.append vai criar as listas
# if resposta para continuar cadastrando pessoas
# for vai pegar o indice e nome na ficha
# print aluno[0] para pegar o nome e aluno[2] para pegar a media
# while para mostra a nota de um aluno em especifico
#if opcao para mostrar de outro aluno
# if len(ficha) para buscar a nota media
# print ficha[opcao][0] para pegar o nome da ficha
# print ficha[opcao][1] para pegar as notas.