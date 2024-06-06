# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso,
# você deve mostrar, para cada palavra,quais são as suas vogais.

palavras = ("aprender", "programar", "linguagem", "python"
            "curso", "gratis", "estudar", "praticar",
            "trabalhar", "mercado", "programador", "futuro")
for p in palavras:
    print(f"\nNa palavras {p.upper()} temos", end=" ")
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra, end=" ")

# ------------- fim do codigo ------------- #
# for para percorrer todas as palavras
# p para cada palavra
# o segundo for para contar as vogais