# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# feito com a cotação do dia 22/04/2024 

Real = float(input("Digite quanto dinheiro voce tem carteira ? "))
dolar = Real / 5.17
euro = Real / 5.50
ars = Real * 168.77

print(f"""Com R$ {Real:.2f} voce pode comprar:
    Dolar {dolar:.2f}
    Euro {euro:.2f}
    Peso Argentino {ars:.2f}
    """)
# Foi usado aspas triplas p quebrar a linha