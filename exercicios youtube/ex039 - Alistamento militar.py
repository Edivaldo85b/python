 # Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
 # se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
 # Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
ano = date.today().year
nascimento = int(input("Ano de nascimento? "))
idade = ano - nascimento

print(f"Quem nasceu em {nascimento} tem {idade} anos em {ano}")
if idade == 18:
    print(" Você deve se alistar imediatamente ! ")
elif idade < 18:
    saldo = 18 - idade
    falta = ano + saldo
    print(f"Ainda falta {saldo} anos para o alistamento")
    print(f"Seu alistamento será em {falta}")
elif idade > 18:
    saldo = idade - 18
    ali = nascimento + 18
    print(f"Você ja deveria ter se alistado há {saldo} anos.")
    print(f"Você ja deveria ter se alistado no ano {ali}.")
    
#---------- fim do codigo ----------#
# primeiro print somente para iformacao
# foi feito com elif para melhor visualizacao do codigo
# importado a biblioteca datetime ,mas somente a data para pode usar o ano atual.
# idade para mostrar a idade atual
# saldo para saber o tempo que falta e o que passou
# ali o ano que deveria ter feito o alistamento