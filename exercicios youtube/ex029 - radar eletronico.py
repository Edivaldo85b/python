# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
# mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.

km = 80
velocidade = float(input("Qual a velocidade do carro ? : "))

if velocidade > 80 :
    km = (velocidade - km) * 7
    print (f"Você foi multado, o valor a ser pagao é {km:.2f} ")
else:
    print("Parabens Você esta dentro da velocidade permitida")
    
#---------- fim do codigo ----------#

# definido o km para iniciar com 80 por ser o limite de velocidade
# dentro do if o km recebeu somente o valor da diferença de velocidade pq foi diminiudo do valor digitado

# no video foi feito de uma forma diferente.
# dentro do if foi criado a multa e foi diminiudo da velocidade - 80 para chegar na diferença.
#tbm nao foi criado o else.