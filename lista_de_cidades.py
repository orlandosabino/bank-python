lista = []
insira = input("digite o nome da da primeira cidade: ")
insira2 = input("digite o nome da segunda cidade:")
insira3 = input("digite o nome da terceira cidade: ")
insira4 = input("digite o nome da quarta cidade: ")
insira5 = input("digite o nome da quinta cidade: ")
lista.append (insira)
lista.append (insira2)
lista.append (insira3)
lista.append (insira4)
lista.append (insira5)
for i in range(len(lista)):
    print(lista[i])