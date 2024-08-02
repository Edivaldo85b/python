# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar
# um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.


def notas(*varias_notas, sit= False):
    """
    => Funcao para analisar notas de varios alunos.
    :param varias_notas: uma ou mais notas de alunos.
    :param sit: valor opcional, indicando se deve ou não adicionar a Situação.
    :return: dicionáriocom varias informações sobre a Situação da turma.
    """
    
    resposta= {}
    resposta["Total"] = len(varias_notas)
    resposta["Maior"] = max(varias_notas)
    resposta["Menor"] = min(varias_notas)
    resposta["Media"] = sum(varias_notas) / len(varias_notas)
    if sit:
        if resposta["Media"]>= 7:
            resposta["Situação"] = "Boa"
        elif resposta["Media"] >= 5:
            resposta["Situação"] = "Razoavel"
        else:
            resposta["Situação"] = "Ruim"
    return resposta
    
    
resp = notas(9, 10, 5.5, 2.5, 8.5, sit=True)
print(resp)

# ---------------- Fim do codigo ---------------- #
#definimos notas com varias_notas e a Situação comeca oculto
# Total é Quantidade de elemento, Maior elemento,Menor elemento,media é soma de elemento divido pela quantia de elemento
# if testa a Situação das notas
# print retorna o dicionario com as notas.