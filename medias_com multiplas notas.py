nome = input("digite seu nome")
notas = 0.0
contador=0
while True:
    menu=int(input("digite 1 para inserir a nota \ndigite 0 para encerrar"))
    if menu == 0:
        print ("o programa será encerrado")
        break
    elif menu == 1:
        contador+=1
        nota = float(input("digite sua nota: "))
        notas+=nota
media=notas/contador        
        


       