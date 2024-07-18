# Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
 
def escreva (mensagem):
    tamanho = len(mensagem) + 2
    print("~"*tamanho)
    print(mensagem)
    print("~"*tamanho)
    
escreva("  Gustagavo Guanabara")
escreva("  Curso de Python no Youtube")
escreva("  oi")

# ------------- Fim do Codigo ------------- #
#foi definido a funcao escreva e dentro do parenteses a mensagem que será mpstrada
# variavel tamanho vai ler o tamanho da mensagem e adicionar mais dois ~~
#no print o ~ foi multiplicado por tamanho da frase.