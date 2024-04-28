# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza (primeiro = Ana; último = Souza.

nome = str(input("digite seu nome completo: ")).strip().upper()
nome = nome.split()
print(f"""O seu primeiro nome é {nome[0]}
O seu ultimo nome é {nome[len(nome)-1]}""")

#---------- Fim do codigo ----------#

# foi criado uma nova variavel divida por split
# foi usado len nome - 1 para pegar o ultimo nome