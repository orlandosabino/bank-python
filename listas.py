mercado = ["arroz", "feijão", "frutas"]
mercado.append ("macarrão")
mercado.append ("açúcar")
mercado.pop (1)
mercado.remove("frutas")
for i in range (len(mercado)):
    print(mercado[i])

print(mercado[2]) 
for i in range (len(mercado)):
    if mercado[i]=="arroz":
        print ("arroz existe")
        break
mercado.append("óleo")
mercado.append("manteiga")
mercado.append("cerveja")
print(mercado[0:3])
print(mercado[3:5])
print(mercado[2:])
print(mercado[:3])
for m in mercado:
    print(m) 