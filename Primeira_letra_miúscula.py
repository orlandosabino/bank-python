#Converta a primeira letra de cada palavra em maiúscula
nomes = ["joão", "maria", "laura", "amélia"]  
resultado = []
for nome in nomes:
    resultado.append(nome[0].upper() + nome[1:])
print(resultado)    