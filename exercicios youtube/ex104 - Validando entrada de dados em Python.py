# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n: ')

def leiaInt(mensagem):
    ok= False
    valor=0
    while True:
        numero = str(input(mensagem))
        if numero.isnumeric():
            valor = int(numero)
            ok = True
        else:
            print("Erro digite um numero inteiro valido !!!")
        if ok:
            break
    return valor
    

Numero_lido = leiaInt("digite um numero: ")
print(f"Voce acabou de digitar o numero {Numero_lido}")

# ------------ fim do codigo ------------ #
# definimos leiaInt para receber uma mensagem
# iniciamos ok como falso e o valor com zero para usar no while
# numero recebe uma string para pode fazer a validação.
# if com isnumeric testa se é um numero inteiro e mudo ok para verdadeiro senão da erro e pede p digitar novamente
# if ok encerra o loop caso verdadeiro
# return ira retornar o valor digitado
# Numero_lido é a mensagem do def
#print mostra o numero inteiro digitado