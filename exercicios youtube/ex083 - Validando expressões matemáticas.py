# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
expressao = str(input("Digite uma expressão: "))
pilha = []
for simbolo in expressao :
    if simbolo == "(":
        pilha.append("(")
    
    elif simbolo == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break
if len(pilha) == 0 :
    print("Sua expressão está valida !")
else:
    print("Sua expressão está errada !")
    
    
    
    
    
# for foi criado para verificar o simbolo na expressão
# if foi criado para verificar se é parênteses aberto
# dentro do if ira pegar os parênteses aberto
# elif foi criado para verificar se é parênteses fechado.
# dentro do elif destamos se a lista esta vazia,senao tiver vazia adiciona o parênteses fechado.
# no if fora do laca testamos se tem a mesma quantidade de parênteses 
# no else senao tiver a mesma quantidade ira apresentar o erro
