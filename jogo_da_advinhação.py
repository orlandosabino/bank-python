numero_secreto = 7
palpite = int(input("Adivinhe o número secreto (1 a 10): "))

while palpite != numero_secreto:
    print("Errado, tente novaente!")
    palpite = int(input("Adivinhe o número secreto (1 a 10): "))

print("Parabéns, você  acertou!")    
