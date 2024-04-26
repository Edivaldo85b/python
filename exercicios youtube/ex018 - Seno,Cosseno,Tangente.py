# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan
angulo = float(input("Digite o angulo: "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f"""O angulo {angulo} tem:
         O Seno de {seno:.2f}
         O Cosseno de {cosseno:.2f}
         A Tangente de {tangente:.2f}""")
         
#---------- Fim do codigo ----------#
 # foi importado da biblioteca math o radiano seno e cosseno e tangente
 # foi convertido o angulo em radiano para depois calcular o seno,cosseno,tangente