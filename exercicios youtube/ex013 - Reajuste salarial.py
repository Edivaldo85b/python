# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Qual é o salário do funcionário? R$: ")) # float foi usado para digitar os centavos
aumento = salario + (salario * 0.15) # o 15% foi feito em formato decimal para facilitar o codigo,
# primeiro irá fazer a conta dos 15% depois ira somar com salario.
print(f"Um funcionário que ganhava {salario:.2f}, com 15% de aumento, passará a ganhar {aumento:.2f}")

#---------- Fim do codigo ----------#