saldo = 5000.0
while True:
    menu=int(input("digite 0 para encerrar o programa \ndigite1 digite 1 para realizar um débito \ndigite2 digite 2 para realizar um crédito \ndigite3 digite 3 para mostrar o saldo"))
    if menu == 0 :
        print ("o programa está sendo encerrado")
        break
    elif menu == 3:
        print(f"{saldo} é o saldo")
    elif menu == 1:
        debito = float(input("digite o valor que você quer debitar: "))
        if debito <=0:
            print("valor inválido")
        elif debito > saldo:
            print("saldo insuficiente")  
        else:
            saldo-= debito
            print(f"debito realizado com sucesso! Seu novo saldo é: R$ {saldo: .2f}")
    elif menu == 2:
        credito = float(input("digite o valor que você quer creditar:"))   
        if credito <= 0:
            print ("valor inválido")     
        else:
            saldo += credito
            print (f"credito realizado com sucesso! Seu novo saldo é:R$ {saldo:.2f}")    
 