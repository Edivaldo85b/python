# Faça um programa que tenha uma função chamada área(), 
# que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.

def area(Largura, Comprimento):
    area_total = Largura * Comprimento
    print(f"A area {Largura:.2f} x {Comprimento:.2f} é de {area_total:.2f}m2.")


print("Controle de Terrenos")
print("-"*20)
L = float(input("Largura (m): "))
C = float(input("Comprimento (m): "))
area(L, C)

# ------------- Fim do codigo ------------- #
# def area cria a função
# dentro do parenteses usamos o parametro largura e Comprimento
# area_total vai fazer a conta do terreno
# print formatado para visualizar o resultado
# variaveis L , C para receber o tamanho do terreno
#area para chamar a funcao e dentgro do parenteses as variaveis L, C para ser passado na função