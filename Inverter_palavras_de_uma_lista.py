# Dada uma lista de palavras, crie uma nova lista com cada palavra invertida.
palavras = ["python", "lista", "string", "for"]
invertidas = []
for palavra in palavras:
    invertidas.append(palavra[::-1])

print(invertidas)    