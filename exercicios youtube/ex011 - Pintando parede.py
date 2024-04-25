# Faça um programa que leia a largura e a altura de uma parede em metros, 
# calcule a sua área e a quantidade de tinta necessária para pintá-la, 
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura  = float(input("Digite a largura da parede: ")) #foi usado float para que o usuario poder digitar numero decimal
altura = float(input("Digite a altura da parede: "))
area = largura * altura # foi multiplicado um pelo outro par ter a area da parede
tinta = area /2 # foi divido por 2 pq cada litro de tinta faz 2 mts quadrados

print(f"Sua parede tem a dimensão de {largura} x {altura} e sua area é de {area:.2f}m².")
print(f"Para pintar essa parede, você precisará de {tinta:.2f}L de tinta. ")

#---------- Fim do codigo ----------#