# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado 
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, 
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

carro = int(input("Quantos dias o carro foi alugado ? ")) # int pq os dias nao pode ser fracionado
km = float(input("Quantos KM rodados ? ")) # float pq os kms podem ser fracionado
total = (carro * 60) + (km * 0.15) # vai ser feito separado o valor de dias e depois vair fazer o valor de km ai soma os dois

print(f"O total a pagar é R$ {total:.2f}")


#---------- Fim do codigo ----------#