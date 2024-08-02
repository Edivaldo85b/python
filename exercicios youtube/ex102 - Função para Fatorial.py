# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) 
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(numero, show=False):
    """
    -> Calcula o Fatorial de um numero.
    :parâmetro n: O numero a ser calculado:
    :parâmetro show:(opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um numero n.
    """
    Fatorial = 1
    for contador in range(numero, 0, -1):
        if show:
            print(contador, end=" ")
            if contador > 1 :
                print("X", end=" ")
            else:
                print("=", end=" ")
        Fatorial = Fatorial * contador
    return Fatorial


print(fatorial(5, show=True))

# ------------- fim do codigo ------------- #
# nas aspas triplas foi colocado as docstrings
# for vai comecar do numero fatorial até o zero voltando de um em um
# if vai x entre os numeros maiores q 1 e o igual se for zero
