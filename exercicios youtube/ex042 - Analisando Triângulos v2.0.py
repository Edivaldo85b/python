# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

print(f"{'-=-'*10}\n Analisador de triângulo\n{'-=-'*10}")

seg1 = float(input("digite o primeiro seguimento: "))
seg2 = float(input("digite o segundo seguimento: "))
seg3 = float(input("digite o terceiro seguimento: "))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg2 + seg1:
    print("Os seguimentos podem FORMAR um triangulo" , end=' ')
    if seg1 == seg2 == seg3:
        print('EQUILÁTERO')
    elif seg1 != seg2 != seg3 != seg1:
        print("ESCALENO")
    else:
        print("ISÓSCELES")
else:
    print("Os seguimentos NÂO PODEM FORMAR um triangulo")
    
#---------- fim do codigo ----------#

# foi acrescentado mais funções no codigo adicionando ISÓSCELES,ESCALENO,EQUILÁTERO
# foi usado if dentro de if para continuar testando