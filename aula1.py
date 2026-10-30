nome = input("digite seu nome")
idade = int(input("digite sua idade"))

if idade >= 21:
    print (f"{nome} responsável pelos outros") 
elif idade >=18:
    print (f"{nome} maior de idade")  
else:
    print (f"{nome} menor de idade")    

 