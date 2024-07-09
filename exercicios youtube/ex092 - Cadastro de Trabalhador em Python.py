# Crie um programa que laia nome, ano de nascimento a carteira de
# trabalho e Cadastre-os (com idade) em um dicionário se por
# acaso a CTPS for difarente de ZERO, o dicionário receberá
# também o ano de contratação e o salário. Calcula e acrescanta,
# além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

dados = {}
dados["Nome"] = str(input("Nome: "))
nascimento = int(input("Ano de Nascimento: "))
dados["Idade"] = datetime.now().year - nascimento
dados["ctps"] = int(input("Carteira de Trabalho ( 0 nao tem ): "))
if dados["ctps"] != 0:
    dados["Contratação"] = int(input("Ano de Contratação: "))
    dados["Salario"] = float(input("Salario: R$"))
    dados["Aposentadoria"] = dados["Idade"] + ((dados["Contratação"] + 35) - datetime.now().year)
print("-="*30)
for chave, valor in dados.items():
    print(f"  - {chave} tem o valor {valor}")
    
# -------------- fim do codigo -------------- #
# foi importado datetime para pegar o ano atual
# nascimento foi declarado em variavel simples para depois jogar dentro do dicionário
# ja fazendo o calculo para se transformar na idade
# o if vai encerrar caso seja zero na carteira de Trabalho
# o print doi formatado com chave e valor para melhor visualização