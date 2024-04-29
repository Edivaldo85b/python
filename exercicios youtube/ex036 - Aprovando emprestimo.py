# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input("Qual o valor da casa ? "))
salario = float(input("Qual seu salario ? "))
anos = float(input("Em quantos ano vai ser o pagamento ? "))
minimo = salario * 0.30
prestacao = casa / (anos * 12)

print(f"Para pagar uma case de {casa:.2f} em {anos}anos a parcela sera de {prestacao:.2f}", end="")
if prestacao <= minimo:
    print(" seu empréstimo foi APROVADO")
else:
    print(" seu empréstimo foi NEGADO")
    
#---------- fim do codigo ----------#

# minimo usado para descobrir o valor minimo da parcela
# prestacao vai ser calculado a qntia de anos *12 para chegar na qntia de meses
# depois vai ser dividido pelo valor da casa para saber a parcela
# if testa para saber se o valor da prestacao é menor ou igual ao valor minimo do salario