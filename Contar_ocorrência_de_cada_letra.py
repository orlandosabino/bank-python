# Conte quantas vezes uma letra aparece em uma palavra
palavra = "banana"
contagem = {}

for letra in palavra:
    if letra in contagem:
        contagem[letra] += 1
    else:
        contagem[letra] = 1    

print(contagem)         
