# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print(f"{'-=-'*10}\n Analisador de triângulo\n{'-=-'*10}")

seg1 = float(input("digite o primeiro seguimento: "))
seg2 = float(input("digite o segundo seguimento: "))
seg3 = float(input("digite o terceiro seguimento: "))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg2 + seg1:
    print("Os seguimentos podem FORMAR um triangulo")
else:
    print("Os seguimentos NÂO PODEM FORMAR um triangulo")
    
#---------- fim do codigo ----------#

# cada seguimentos tem q ser menor q a soma dos outros dois para formar o triangulo