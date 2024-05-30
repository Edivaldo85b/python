# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. 
# O programa encerrará quando ele disser que quer mostrar 0 termos.

print('Gerador de PA')
print('-='*10)
primeiro = int(input("Primeiro Termo: "))
razao = int(input("Razao da PA: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f"{termo} -> ", end="")
        termo = termo + razao
        cont = cont + 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais ? "))
print(f"Progressao finalizada com {total} termos mostrados")
print("FIM")
    
# -------------- Fim do codigo -------------- #

#variavel termo para comecar a contar os termos e a variavel cont para contar quantos termos foram
# variavel total comeca com zero para o usuário digitar a quantidade que ele quer
#varial mais comeca com 10 pq a primeira vez o programa mostra 10
# dentro do while o total vai passar a receber toda a quantidade termos