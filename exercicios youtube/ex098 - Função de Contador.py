# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
# início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

from time import sleep


def contador(incio, fim, passo):
    if passo < 0:
        passo = passo * -1
    if passo == 0:
        passo = 1
    print("-="*20)
    print(f"Contagem de {incio} ate {fim} de {passo} em {passo}.")
    sleep(2.0)
    
    
    if incio < fim:
        Contagem = incio
        while Contagem <= fim:
            print(f"{Contagem} ", end=" ", flush=True)
            sleep(0.5)
            Contagem = Contagem + passo
        print("Fim !!!")
    else:
        Contagem = incio
        while Contagem >= fim:
            print(f"{Contagem} ", end=" ", flush=True)
            sleep(0.5)
            Contagem = Contagem - passo
        print("Fim !!!")
    

contador(1, 10, 1)
contador(10, 0, 2)
print("-="*20)
print("Agora é sua vez de personalizar:")
comecar = int(input("Incio: "))
terminar = int(input("Fim: "))
pulo = int(input("Passo: "))
contador(comecar, terminar, pulo)

# -------------- Fim do codigo -------------- #
# foi importado sleep da biblioteca time para fazer a Contagem de segundos entre mostrar os numeros
# foi definido a função de contar com inicio fim e o passo.
# if <0 vai testar se o numero é negativo para fazer a contagem do passo
# if == 0 vai contar de 1 em 1 para não travar o programa
# if inicio < fim o while vai fazer a contagem positiva do passo
# o flush = True faz a contagemser mostrada e nao armazenada no buffer
# else: o while faz a contagem negativa do passo
# foi criado as variaveis, comecar,terminar,pulo , para fazer a contagem personalizada