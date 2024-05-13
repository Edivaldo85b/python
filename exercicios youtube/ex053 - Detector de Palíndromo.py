# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

# Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso =' '

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo ')
else:
    print('A frase digitada não é um palíndromo !')
        
# ------------- fim do codigo ------------- #

# split separa as palavras em uma lista
# join para juntar as letras
# no lugar do contador foi usado letra

# depois foi ensinado a fazer sem o loop do for
# inverso = junto[::-1] que facilitaria muito o codigo mas como a aula era de for
#achei melhor manter o codigo em for