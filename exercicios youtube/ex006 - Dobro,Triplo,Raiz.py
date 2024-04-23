# Crie um algoritimo que leia um numero e mostre o seu dobro, triplo e a raiz quadrada.
numero = int(input("Digite um numero: ")) # foi criado a variavel numero para armazenar o numero
dobro = numero * 2 # foi criado a variavel dobro para fazer a conta e armazenar o dobro do numero
triplo = numero * 3 # foi criado a variavel triplo para fazer a conta e armazenar o triplo do numero
raiz = numero ** (1/2) # foi criado a variavel raiz para fazer a conta e armazenar a raiz quadrada do numero

print(f"O dobro de {numero} é : {dobro}\nO triplo de {numero} é : {triplo}\nA raiz quadrada de {numero} é : {raiz:.2f}")
# poderia ter sido feito as contas dentro do print ,mas ai não seria armazenado os resultados

# print(f"O dobro de {numero} é : {numero *2}\n O triplo de {numero} é : {numero *3}\n A raiz quadrada de {numero} é : {numero **(1/2):.2f}")

