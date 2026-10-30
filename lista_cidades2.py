Lista = []
quantidade = int(input("Quantas cidades deseja cadastrar? "))
for i in range(quantidade):
    cidade = input(f"Digite o nome da {i+1}º cidade: ")
    Lista.append(cidade)
print("\nCidades cadastradas: ")
for cidade in Lista:
    print(cidade)    
