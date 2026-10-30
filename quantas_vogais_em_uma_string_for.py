# Conte quantas vogais existem em uma string usando "for".
texto = "Programação em python"
vogais = "aeiouAEIOU"
contador = 0

for letra in texto:
    if letra in vogais:
        contador += 1

print(f"Total de vogais: {contador}")