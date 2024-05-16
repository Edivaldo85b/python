# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa

from time import sleep

opcao = 0
numero1 = int(input('Primeiro valor: '))
numero2 = int(input('Segundo valor: '))

while opcao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    
    if opcao == 1:
        soma = numero1 + numero2
        print('A soma entre {} e {} é {}'.format(numero1, numero2, soma))
    elif opcao == 2:
        produto = numero1 * numero2
        print('O resultado de {} x {} é {}'.format(numero1, numero2, produto))
    elif opcao == 3:
        if numero1 > numero2:
            maior = numero1
        else:
            maior = numero2
        print('Entre {} e {} o maior valor é {}'.format(numero1, numero2, maior))
    elif opcao == 4:
        print('Informe os números novamente:')
        numero1 = int(input('Primeiro valor: '))
        numero2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')

# ------------------- Fim do codigo ------------------- #
# dentro de cada if e elif foi criado as opções
# no else foi criado caso seja digitado um numero diferente do menu