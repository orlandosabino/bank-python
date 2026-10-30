nome = input("Qual é o seu nome? ")
quantidade = int(input("Quantos sorvetes você comprou? "))
preco_unitario = float(input("Qual é o preço de cada sorvete? "))
total = quantidade * preco_unitario
if quantidade >=3:
    desconto = total * 0.05
    total -= desconto
    print(f"\nParabéns {nome}, você ganhou 5% de desconto!")
else:
    print(f"\nObrigado pela compra, {nome}!")  
print(f"Valor final da compra: R$ {total:.2f}")                  