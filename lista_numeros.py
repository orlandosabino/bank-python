numeros = [5, 10, 15, 23, 54, 32, 56, 95, 43]
soma = 0
for num in numeros:
    soma += num
print("A soma total é:", soma)   
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))
numero4 = int(input("Digite o quarto numero: "))
numero5 = int(input("Digite o quinto numero: "))
lista = []
lista.append(numero1)
lista.append(numero2)
lista.append(numero3)
lista.append(numero4)
lista.append(numero5)
soma_lista = 0
for i in range(len(lista)):
    if lista [i] % 2 == 0:
       soma_lista += lista [i]
print("A soma total é:", soma_lista)  



