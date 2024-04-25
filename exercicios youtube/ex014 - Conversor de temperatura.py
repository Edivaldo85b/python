# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
celcius  = float(input("Digite a temperaturaem graus Celsius: ")) # float para usar decimal
# f  = 9 * c / 5 + 32 # no video foi usado essa formula
Fahrenheit = celcius * 1.8 + 32 # achei essa formula na internet , que considerei mais smples de fazer o calculo
print(f"A temperatura de {celcius}°C coresponde a {Fahrenheit}°F !")

# ---------- Fim do codigo ----------#