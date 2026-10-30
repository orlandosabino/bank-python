#Perguntar quantidade de produtos
quantidade = int(input("Quantos produtos você vai comprar? "))
#Inicializar total
total = 0
#Loop para somar preços
for i in range(quantidade):
    preco = float(input(f"Digite o preço do produto{i+1}:"))
    total += preco
#Aplicar desconto se total >= 100
if total >= 100:
    desconto = total * 0.10
    total -= desconto
    print("\nVocê ganhou 10% de desconto!")
#Mostrar resultado
print (f"Valor final da compra: R${total:.2f}")    

