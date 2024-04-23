# Desenvolva um Programa que leia as duas notas de um aluno,calcule e mostre sua media.
Nota1 = float(input("Digite a sua primeira nota: ")) # foi criado a variavel nota 1 para receber a nota
Nota2 = float(input("Digite a sua segunda nota: "))# foi criado a variavel nota 1 para receber a nota
# foi usado float par o usuario poder digitar um numero flutuante,ou seja com ponto ,ja que nao pode ser usado virgula em python
media = (Nota1 + Nota2) /2 # doi criado media para armazenar a media
#foi colocado parenteses no Nota1 e Nota2 para fazer a conta de soma antes da divisão seguindo a regra matematica

print(f"A media entre {Nota1:.1f} e {Nota2:.1f} é igual = {media:.1f}")

# novamente a conta poderia ser feita dentro do print ,mas ai não iria armazenara conta

#print(f"A media entre {Nota1:.1f} e {Nota2:.1f} é igual = {(Nota1+Nota2)/2:.1f}")