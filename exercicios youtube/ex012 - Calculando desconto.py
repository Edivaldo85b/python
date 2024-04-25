#  Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input("Qual o preço do produto ? R$: ")) # float foi usar para pode digitar os centavos
desconto = preco - (preco *0.05) # vai ser feito a conta de 5% primeiro,
# sendo que foi digitado em decimal para facilitar na conta,depois irá reduzir do preco original.
print(f"O produto que custava {preco}, na promoção com desconto de 5% vai custar {desconto:.2f}")

#---------- Fim do codigo ----------#