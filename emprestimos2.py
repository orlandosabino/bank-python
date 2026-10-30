salario = float (input("digite o valor do salario: "))
moradia = float (input("quanto você gasta com moradia: "))
despesasfixas = float(input("valor das despesas fixas: "))
valordocarro = float(input("qual o valor do carro que você quer comprar: "))
prestacao = 0
if valordocarro <= 10000:
    print (" máximo de 48 prestações")
    prestacao = 48    
elif valordocarro <= 30000:
    print ("máximo 60 prestações")
    prestacao = 60   
elif valordocarro >= 100000:
    print ("máximo de 120 prestações")
    prestacao =120
confirmacao = (input("digite sim ou não se você concorda com o número de prestações: "))
if confirmacao == "sim": 
    valor_prestacao = valordocarro/prestacao
else:
    print("valor encerrado")
    
    
  
