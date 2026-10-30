saldo = 5000
debito = float( input("digite o valor que você quer debitar: "))
if debito <= 0:
    print("valor inválido")
elif debito > saldo:
    print("saldo insuficiente")
else:
    saldo -= debito # significa saldo = saldo - debito
    print(f"debito realizado com sucesso! Seu novo saldo é: R$ {saldo: .2f}")   