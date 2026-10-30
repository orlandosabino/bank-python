saldo = 1000.0
while True:
    menu = int(input("digite 0 para encerrar o programa \n digite 1 para realizar debito \n digite 2 para realizar credito \n digite 3 para saldo" ))
    if menu == 0 :
        print ("o programaestá sendo encerrado")
        break
    elif menu == 1 :
        debito = float (input("digite o valor que você quer debitar:"))
        if debito <= 0:
            print ("valor inválido")
        elif debito > saldo:
            print("saldo insuficiente")
        else: 
            saldo-=debito
            print(f"débito realizado com sucesso! Seu novo saldo é: R$ {saldo: .2f}") 
    elif menu == 2 :
        credito = float (input("digite o valor que você quer creditar:"))
        if credito <= 0:
            print ("valor inválido")
        else:
            saldo += credito
            print(f"credito realizado com sucesso! Seu novo saldo é: R$ {saldo: .2f}")
    elif menu == 3:
        print (f" o seu novo saldo é: R$ {saldo: .2f}")
          
        
            


        