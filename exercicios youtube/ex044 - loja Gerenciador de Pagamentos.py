# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros


print('{:=^40}'.format(' LOJA FISH '))

preco = float(input("Preço das compras: R$ "))
print("""FORMAS DE PAGAMENTO
[1] À vista dinheiro/cheque
[2] À vista no cartão
[3] Em até 2x no cartão
[4] 3x ou mais no cartão""")
opcao = int(input("Qual a opção ? "))

if opcao == 1:
    total = preco - (preco * 0.1)
elif opcao == 2:
    total = preco - (preco *0.05)
elif opcao == 3:
    total = preco
    parcela = preco / 2
    print(f'A sua compra será parcelado em 2x {parcela}')
elif opcao == 4:
    total = preco + (preco * 0.2)
    parcelamento = int(input("Quantas Parcelas ?: "))
    parcela = total / parcelamento
    print(f'Sua compra seá parcelada em {parcelamento}x de R${parcela} com juros')
else:
    total = preco
    print("Opção INVALIDA de pagamento, tente novamente")
print(f'A sua compra de R$:{preco:.2f} vai custar R$:{total:.2f} no final')

