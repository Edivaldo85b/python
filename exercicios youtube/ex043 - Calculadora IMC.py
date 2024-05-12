# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

imc = peso / altura ** 2

print ('Seu IMC é: %.1f' % imc)

if imc < 16:
    print ('Magresa grave, procure um medico URGENTE')
elif imc > 16 and imc < 17: 
    print ('Magresa moderada, procure um medico')
elif imc > 17 and imc < 18.5: 
    print ('Magresa leve')
elif imc > 18.51 and imc < 25: 
    print ('Parabens você esta saudável')
elif imc > 25 and imc < 30: 
    print ('Sobrepeso')
elif imc > 30.01 and imc < 35: 
    print ('Sobrepeso 2, procure um medico')
elif imc > 35.01 and imc < 40: 
    print ('Obesidade Grau 1, procure um medico')
else: 
    print ('Obesidade Grau 2, procure um medico URGENTE')

#---------- Fim do codigo ----------#