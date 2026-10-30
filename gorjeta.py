nome = input("qual é seu nome? ")
valor_conta = float(input("Qual o valor total da conta? "))
pessoas = int(input("Quantas pessoas vão dividir a conta? "))
gorjeta = valor_conta * 0.10 
total_com_gorjeta = valor_conta + gorjeta
valor_por_pessoa = total_com_gorjeta/pessoas
print(f"\n Olá {nome}!")
print(f"total com gorjeta: R$ {total_com_gorjeta:.2f}" )
print(f"cada pessoa paga: R$ {valor_por_pessoa:.2f}" )