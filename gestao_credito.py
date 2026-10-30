saldo = 5000
credito = float(input("digite o valor que você quer creditar: "))
if credito <= 0:
    print (" valor inválido")
else:
    saldo += credito
    print (f" crédito realizado com sucesso! Seu novo saldo é: R$ {saldo: .2f}")