#Remova itens repetidos de uma lista
itens = ["a","b", "a", "c","d","b", "a", "c"]
unicos = []

for item in itens:
    if item not in unicos:
        unicos.append(item)
print (unicos)        
