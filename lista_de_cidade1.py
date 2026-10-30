lista = []
for i in range (5):
    cidade = input(f"Digite o nome da {i+1}º cidade: ")
    lista.append(cidade)
print("\nCidades cadastradas: ")   
for cidade in lista:
    print(cidade)
