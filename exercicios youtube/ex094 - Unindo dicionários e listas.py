#Cria um programa que leia nome, sexo a idade de várias passoas guardando os dados de cada passoa
# em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas passoas cadastradas
# B) A média da idada.
# C) Uma lista com mulheres.
# D) Uma lista com idade acima da média.
galera = []
pessoa = {}
soma_idade = media_idade = 0
while True:
    pessoa.clear()
    pessoa["Nome"] = str(input("Nome: "))
    while True:
        pessoa["Sexo"] = str(input("Sexo: [M/F]")).upper()[0]
        if pessoa["Sexo"] in "MF":
            break
        print("ERRO !!! Por favor, digite apenas M ou F .")
    pessoa["Idade"] = int(input("Idade: "))
    soma_idade = soma_idade + pessoa["Idade"]
    galera.append(pessoa.copy())
    while True:
        resposta = str(input("Quer continuar ? [S/N]")).upper()[0]
        if resposta in "SN":
            break
        print("ERRO !!! Por favor, responda apenas S ou N .")
    if resposta == "N" :
        break
print("-="*30)
print(f"A) Ao todo temos {len(galera)} pessoas cadastradas.")
media_idade = soma_idade / len(galera)
print(f"B) A media de idade é de {media_idade:5.2f} anos.")
print("C) As mulheres cadastradas foram ", end =" ")
for mulheres in galera:
    if mulheres["Sexo"] in "Ff":
        print(f"{mulheres['Nome']}", end=" ")
print()
print("D) Lista de pessoas acima da media: ")
for acima_da_media in galera:
    if acima_da_media["Idade"] >= media_idade:
        print("    ", end= " ")
        for chave, valor in acima_da_media.items():
            print(f"{chave} = {valor}", end=" ")
        print()
print("<< ENCERRADO >>")

# -------------- fim do codigo -------------- #
# foi criado a lista galera vazio e o dicionário pessoa vazia
# while True vai fazer a leitura dos dados das pessoas
#o if vai testar masculino e femenino ,se digitar outra coisa vai retornar a pergunta
# se marcar m ou f vai proceguir e perguntar a idade
# soma_idade , vai fazer a somada das idades das pessoas
# galera.append(pessoa.copy()) vai copiar o dicionário pessoa para lista galera
# vai iniciar outro while perguntando se deseja continuar
# na letra a len(galera) vai mostra a quantidade de pessoas cadastradas
# media_idade vai receber a soma das idades e dividir pela quantidade de pessoas
# e vai ser mostrado na letra b
# na letra c vai mostrar as mulheres cadastradas
# na letra d o for vai passar pelas idades e pegar as idades igual e maior que a media_idade
# o print vai mostrar as chaves e valores formatados