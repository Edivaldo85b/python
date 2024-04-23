# Escreva um programa que leia um valor em metros e exiba convertido em centimetros e milimetros
# KM HM DAM M DM CM MM

metros = float(input("Digite uma distancia em metros: "))
km = metros / 1000
hm = metros / 100
dm = metros / 10
dc = metros * 10
cm = metros * 100
mm = metros * 1000

print(f"""A medida em {metros:.1f}m corresponde a:
    {km:.1f} quilometros
    {hm:.1f} hectometros
    {dm:.1f} decametros
    {dc:.1f} decimetros
    {mm:.1f} milimetros
    {cm:.1f} centimetros
    """)