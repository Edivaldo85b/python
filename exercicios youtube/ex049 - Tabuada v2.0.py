# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

numero = int(input('Digite um numero para ver a sua tabuada: '))
for contador in range(1, 11):
    print(f'{numero} x {contador} = {numero * contador}')
    
# -------------- fim do codigo -------------- #

# contador foi até 11 pq dimunui um numero na hora do laço
# dentro do print foi feito a conta para fazer a tabuada