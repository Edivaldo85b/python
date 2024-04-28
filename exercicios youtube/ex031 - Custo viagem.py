# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

passagem = float(input("Qual a distância da viagem ? "))
print(f"Sua viagem terá {passagem} km.")
if passagem < 200:
    print(f"Voce pagará {passagem*0.5:.2f} pela viagem")
    
else:
    print (f"Voce pagará {passagem*0.45:.2f} pela viagem")
    


#---------- fim do codigo ----------#

# o calculo do valor da passagem foi feito dentro do print

# no video foi feito diferente
# foi criado uma variavel para receber o preco no if else e criado o print para puxar o preco