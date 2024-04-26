# Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

from math import hypot
oposto = float(input("Comprimento do cateto oposto: "))
adjacente = float(input("Comprimento do cateto adjacente: "))
hipotenusa = hypot(oposto, adjacente)

print(f"A hipotenusa vai medir {hipotenusa:.2f}")

#---------- Fim do codigo ----------#

# foi importado a hipotenusada biblioteca math
# no Calculo da variavel hipotenusada o hypot faz toda a conta basta colocar os catetos.