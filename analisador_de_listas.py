#Entrada de dados
numeros = [ ]
for i in range(10):
    numero = int(input(f"Digite o {i +1}º: "))
    numeros.append(numero)
#Exibindo a lista original
print("\nlista original:", numeros) 
#Lista invertida
print("Lista invertida:", numeros[::-1])
#soma
print("Soma:", sum(numeros))
#média
print("Média:", sum(numeros ) / len(numeros))
#Maior e Menor
print("Maior número:", max(numeros))
print("Menor número:", min(numeros))
#pares e ímpares
pares = 0
ímpares = 0
for numero in numeros:
    if numero % 2 == 0:
        pares += 1
    else:
        ímpares += 1
print("Quantidade de pares:", pares)
print("quantidade de ímpares:", ímpares)            
#pesquisa
procurado =int(input("\nDigite um número para pesquisar:"))
if procurado in numeros:
    print("Número encontrado!")
    print("Aparece", numeros.count(procurado), "vez(es)")
else:
    print("Número não encontrado!")
#Ordenação
print("Lista ordenada:", sorted(numeros))
#Removendo duplicados
sem_repetidos = list(set(numeros))
print("Lista sem repetidos:", sem_repetidos)         
