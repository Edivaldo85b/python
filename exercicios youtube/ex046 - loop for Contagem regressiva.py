#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

for cont in range (10, -1, -1):
    print(cont)
    sleep(1)
print('BUM!! , BUM!!, POOOWW !!')

#------------- Fim do codigo -------------#

# foi importado sleep para dar uma pausa de um segundo na contagem
# foi colocado -1 para aparecer o zero na contagem e o outro -1 para pode contar ao contrario