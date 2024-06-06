# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
numero = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print(f"Eu sortei os numeros {numero}")
print(f"O maior valor sorteado foi {max(numero)}")
print(f"O menor valor sorteado foi {min(numero)}")

# ------------------- fim do codigo ------------------- #
# foi usado max para pegar o maior valor
# foi usado min para pegar o menor valor