#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(ano):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade < 16:
        return f"Com {idade} anos: NAO VOTA."
    elif 16 <= idade < 18 or idade > 65:
        return f"Com {idade} anos: VOTO OPCIONAL."
    else:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO."


nascimento = int(input("Em que ano voce nasceu? "))
print(voto(nascimento))

# ------------------ Fim do codigo ------------------ #
# foi definido voto e importado a biblioteca datetime dentro dela para economizar espaco na memoria
# a variavel ano_atual vai receber a data atual do computador.
# a variavel idade vai receber o ano_atual menos o ano do nascimento
# if vai testar se a idade é menor que 16 anos
# elif vai testar se a idade é menor que 18 anos e maior que 16 anos
# or vai testar se a idade é maior que 65
# else vai testar se a idade esta entre 18 e 65 anos
# nascimento vai pedir o ano de nascimento e jogar dentro do def para calcular a idade