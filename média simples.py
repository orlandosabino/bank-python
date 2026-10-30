nome = input("digite seu nome")
primeira_nota=float(input("digite a primeira nota:"))
segunda_nota=float(input("digite a segunda nota:"))

media=(primeira_nota+segunda_nota)/2
if media >= 7.0:
    print (f"{nome} foi aprovado com média: {media:.2f}")
elif media >= 5.0:
    print (f"{nome} está em recuperação {media:.2f}")
else:
    print (f"{nome} foi reprovado/a {media:.2f}")    


