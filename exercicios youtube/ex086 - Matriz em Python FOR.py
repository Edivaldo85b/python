# crie um programa que crei uma matriz de dimensão 3x3 e preencha com os valores lido pelo teclado.
# no final mostre a matriz na tela, com a formatação correta

matriz = [[],[],[]]
for linha in range(0,3):
        for coluna in range(0,3):
                matriz[linha].append(int(input(f"Digite um valor para [{linha},{coluna}]: ")))
print('-='*30)
for linha in range(0,3):
        for coluna in range(0,3):
                print(f'[{matriz[linha][coluna]:^5}]', end='')
        print()
        
# ------------------- Fim do codigo ------------------- #
# foi criado o primeiro for para pegar as linhas e antes de ser digitado foi criado
# outro for pagar pegar as colunas, usamos append para pegar os valor

# foi criado outro for para linha e coluna para mostrar no print
# foi centralizado com 5 casas para manter o alinhamento
# o ultimo print para que cada vez q o for passar nele dar uma quebra de linha