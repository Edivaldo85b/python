# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. 
# Para os inferiores ou iguais, o aumento é de 15%.
 
salario = float(input("Qual o salario do funcionário ? R$: "))
 
if salario >= 1250:
    aumento = (salario * 0.10) + salario
    print(f"Quem ganhava {salario:.2f} passa a ganhar {aumento:.2f} agora.")
else:
    aumento = (salario * 0.15) + salario
    print(f"Quem ganhava {salario:.2f} passa a ganhar {aumento:.2f} agora.")
    
#---------- fim do codigo ----------#

#foi usado igual maior caso o salario for exatamente 1250
#a porcentagem foi feito em forma decimal
#poderia ter sido feito o calculo dentro do print